"""
Network and spectrum analysers
"""
from atom.api import Atom, Float, Int, Enum, Bool

import enaml
from enaml.qt.qt_application import QtApplication


from .Instrument import Instrument

class SpectrumAnalyzer(Instrument):
	pass

class NetworkAnalyzer(Instrument):
	power = Float().tag(desc='Output power in dBm')
	centerF = Float().tag(desc='Center Frequency in GHz')
	spanF = Float().tag(desc='Span Frequency in GHz')
	startF = Float().tag(desc='Start Frequency in GHz')
	stopF = Float().tag(desc='Stop Frequency in GHz')
	numPoints = Float().tag(desc='Number of frequency points')
	averages = Int().tag(desc='Number of averages')
	bandwidth = Float().tag(desc='IF Bandwidth in kHz')


class HP71000(Instrument):
	pass

class SpectrumAnalyzer(Instrument):
	# BBN spectrum analyzer
	pass

class HP8563E(Instrument):
	# Matt Lahaye's spectrum analyzer
	pass

class AgilentN5230A(NetworkAnalyzer):
	pass
