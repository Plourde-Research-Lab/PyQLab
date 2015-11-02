from atom.api import Str, Int, Float, Bool, Enum

from Instrument import Instrument

class PulseGenerator(Instrument):
	output = Bool(False).tag(desc='Output enabled')
	mode = Enum('voltage', 'current').tag(desc='Output mode (current or voltage source)')
	value = Float(0.0).tag(desc='Output value (current or voltage)')
	address = String('').tag(desc='VISA address')

class TekAFG3022B(DCSource):

	def json_encode(self, matlabCompatible=False):
		jsonDict = super(TekAFG3022B, self).json_encode(matlabCompatible)
		if matlabCompatible:
			jsonDict['address'] = self.address
		return jsonDict
