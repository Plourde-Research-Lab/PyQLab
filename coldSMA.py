# Copyright (C) 20011  Ted White
# This program is free softe: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Softe Foundation, either version 2 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied ranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import time
import serial as s
import numpy as np
from matplotlib import pyplot as plt
allowedCommands = ['S','R','0','1','2','3','4','5','6',
                   '7','8','9',':',';','<','=','>','?',
                   'a','b','c','d','e','f','g','h','i',
                   'j','k','l','m','n','o','p','q','r']
times = np.linspace(0,21,21)
# configure the serial connections (the ameters differs on the device youe connecting to)
ser = s.Serial(port='COM6',
               baudrate=1200,
               # ity=s.PARITY_NONE, # not needed in python 2.7.1
               stopbits=s.STOPBITS_ONE,
               bytesize=s.EIGHTBITS
               )

print ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input = 1
traceIncrement = 0
output = ''
while 1 :
    # get keybd input
    input = raw_input(">> ")
    if input == 'exit':
        ser.close()
        exit()
        break
    elif input in allowedCommands:
        
        if input == 'S' or input == 'R':
            ser.write(input)
            time.sleep(1)
            out = ''
            currents = []
            while ser.inWaiting() > 0:
                out += ser.read(21)
            if out != '':
                traceIncrement += 1
                output = out
            else:
                print 'no data out'
            for s in range(len(output)):
                current = 4.0*ord(output[s])*(5.0/4095.0)/10.0
                currents.append(current)
            plt.figure()
            plt.xlabel('Time (ms)')
            plt.ylabel('I (mA)')
            plt.title('Trace %d' %traceIncrement)
            plt.plot(times,currents,'b-')
            plt.show()
        else:
            ser.write(input)
        
    else:
        print 'bad command'
              
