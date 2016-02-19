from atom.api import Str, Int, Float, Bool, Enum

from Instrument import Instrument

class PulseGenerator(Instrument):
	output = Bool(False).tag(desc='Output enabled')
	channel = Enum("1", "2").tag(desc='Output channel')
	width = Float(50.0).tag(desc='Pulse Width (us)')
	amp = Float(1.0).tag(desc='Pulse Amplitude (V)')
	delay = Float(0).tag(desc='Pulse Delay (us)')
	address = Str('').tag(desc='VISA address')

class TekAFG3022B(PulseGenerator):

	def json_encode(self, matlabCompatible=False):
		jsonDict = super(TekAFG3022B, self).json_encode(matlabCompatible)
		if matlabCompatible:
			jsonDict['address'] = self.address
			jsonDict['channel'] = self.channel
			jsonDict['width'] = self.width
			jsonDict['amp'] = self.amp
			jsonDict['delay'] = self.delay
		return jsonDict
