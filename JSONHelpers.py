import json, sys

from traits.api import HasTraits

import instruments
from Sweeps import Sweep, SweepLibrary
from MeasFilters import MeasFilterLibrary

from collections import OrderedDict

class LibraryEncoder(json.JSONEncoder):
	"""
	Helper for QLab to encode all the classes we use.
	"""
	def default(self, obj):
		if isinstance(obj, HasTraits):
			tmpDict = obj.__getstate__()

			#Inject the class name for decoding
			tmpDict['__class__'] = obj.__class__.__name__
			tmpDict['__module__'] = obj.__class__.__module__

			#Strip out __traits_version__
			if '__traits_version__' in tmpDict:
				del tmpDict['__traits_version__']

			return tmpDict

		else:
			return super(LibraryEncoder, self).default(obj)

class LibraryDecoder(json.JSONDecoder):

	def __init__(self, **kwargs):
		super(LibraryDecoder, self).__init__(object_hook=self.dict_to_obj, **kwargs)

	def dict_to_obj(self, d):
		if '__class__' in d:
			#Pop the class and module
			className = d.pop('__class__')
			moduleName = d.pop('__module__')
			#Re-encode the strings as ascii (this should go away in Python 3)
			__import__(moduleName)
			args = {k.encode('ascii'):v for k,v in d.items()}
			inst = getattr(sys.modules[moduleName], className)(**args)

			return inst
		else:
			return d

class ScripterEncoder(json.JSONEncoder):
	"""
	Helper for QLab to encode all the classes for the matlab experiment script.
	"""
	def default(self, obj):
		if isinstance(obj, HasTraits):
			#For the instrument library pull out enabled instruments from the dictionary
			if isinstance(obj, instruments.InstrumentManager.InstrumentLibrary):
				tmpDict = {name:instr for name,instr in obj.instrDict.items() if instr.enabled}
			#For the measurment library just pull-out enabled measurements from the filter dictionary
			elif isinstance(obj, MeasFilterLibrary):
				tmpDict = {name:filt for name,filt in obj.filterDict.items() if filt.enabled}
			#For instruments we need to add the Matlab deviceDriver name
			elif isinstance(obj, instruments.Instrument.Instrument):
				tmpDict = obj.__getstate__()
				#If it is an AWG convert channel list into dictionary
				channels = tmpDict.pop('channels', None)
				if channels:
					for ct,chan in enumerate(channels):
						tmpDict['chan_{}'.format(ct+1)] = chan 
				tmpDict['deviceName'] = obj.__class__.__name__
			else:
				tmpDict = obj.__getstate__()

			#Strip out __traits_version__
			if '__traits_version__' in tmpDict:
				del tmpDict['__traits_version__']

			return tmpDict

		else:
			return super(QLabEncoder, self).default(obj)	
	