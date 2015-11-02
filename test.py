# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 11:38:47 2015

@author: Caleb
"""
import h5py # hack until anaconda fixes h5py/pytables conflict
from Libraries import instrumentLib, channelLib
import numpy as np
from QGL import *
import QGL
import config as PQconfig

QGL.Compiler.channelLib = channelLib
QGL.Compiler.instrumentLib = instrumentLib


q1 = QubitFactory('q1')
jpm1 = JPMFactory('jpm1')
seqs = [[JPMMEAS(q1), JPMBias(jpm1, amp=d)] for d in np.linspace(0.1, 1, 11)]
files = compile_to_hardware(seqs, 'MEAS/MEAS')
plot_pulse_files(files)