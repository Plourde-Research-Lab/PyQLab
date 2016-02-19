from Instrument import Instrument

from atom.api import Atom, Str, Int, Float, Bool, Enum, List, Dict, Coerced
import itertools, ast

import enaml
from enaml.qt.qt_application import QtApplication

class Counter(Instrument):
	# """docstring for Counter"""
	# def __init__(self, arg):
	# 	super(Counter, self).__init__()
	# 	self.arg = arg

	address = Str('').tag(desc='USB Port of Arduino')
	repititions = Int(1000).tag(desc='Reptitions per Experiment')
	segments = Int(1).tag(desc='Waveform segments per Experiment')

	def json_encode(self, matlabCompatible=False):
		if matlabCompatible:
			jsonDict = {}
			jsonDict['address'] = self.address
			jsonDict['deviceName'] = 'ArduinoCounter'
			jsonDict['repititions'] = self.repititions
			jsonDict['segments'] = self.segments
		else:
			jsonDict = super(Counter, self).json_encode(matlabCompatible)

		return jsonDict
		