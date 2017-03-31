from atom.api import Str, Int, Float, Bool, Enum

from .Instrument import Instrument

class DCSource(Instrument):
	output = Bool(False).tag(desc='Output enabled')
	mode = Enum('voltage', 'current').tag(desc='Output mode (current or voltage source)')
	value = Float(0.0).tag(desc='Output value (current or voltage)')

class YokoGS200(DCSource):
	outputRange = Enum(1e-3, 10e-3, 100e-3, 200e-3, 1, 10, 30).tag(desc='Output range')

	def json_encode(self, matlabCompatible=False):
		jsonDict = super(YokoGS200, self).json_encode(matlabCompatible)
		if matlabCompatible:
			jsonDict['range'] = jsonDict.pop('outputRange')
		return jsonDict

class SIM928(DCSource):
	ch1Voltage = Float(0.0).tag(desc='SIM channel 1 Voltage')
	ch1Enabled = Bool(True).tag(desc='SIM channel 1 Enabled')
	ch2Voltage = Float(0.0).tag(desc='SIM channel 2 Voltage')
	ch2Enabled = Bool(True).tag(desc='SIM channel 2 Enabled')
	ch3Voltage = Float(0.0).tag(desc='SIM channel 3 Voltage')
	ch3Enabled = Bool(True).tag(desc='SIM channel 3 Enabled')

	# def json_encode(self, matlabCompatible=False):
	# 	jsonDict = super(SIM928, self).json_encode(matlabCompatible)
	# 	jsonDict['channel'] = jsonDict.pop('channel')
	# 	if matlabCompatible:
	# 		jsonDict['range'] = jsonDict.pop('outputRange')
	# 	return jsonDict
