# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 11:38:47 2015

@author: Caleb
"""
#import h5py # hack until anaconda fixes h5py/pytables conflict
from Libraries import instrumentLib, channelLib
#import numpy as np
from QGL import *

Compiler.channelLib = channelLib
Compiler.instrumentLib = instrumentLib


jpm1 = JPMFactory('jpm1')
seqs = [[ JPMBias(jpm1)]]
files = compile_to_hardware(seqs, 'MEAS/MEAS')
plot_pulse_files(files)

#q1 = QubitFactory('q1')
#seqs = [[MEAS(q1)]] 
#files = compile_to_hardware(seqs, 'MEAS/MEAS')
#plot_pulse_files(files)