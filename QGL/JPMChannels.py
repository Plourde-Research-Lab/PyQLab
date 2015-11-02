from Channels import LogicalChannel, LogicalMarkerChannel
import Compiler
import PulseShapes
from DictManager import DictManager
from atom.api import Atom, Str, Unicode, Float, Instance, Property, cached_property, \
                        Dict, Enum, Bool, Typed, observe

class JPM(LogicalChannel):
    """A class for JPM Channels"""
    pulseParams = Dict(default={'length':5e-9, 'amp':1.0, 'shapeFun':PulseShapes.gaussian, 'buffer':0.0, 'cutoff':2, 'dragScaling':0, 'sigma':5e-9})
    gateChan = Instance((unicode, LogicalMarkerChannel))

    def __init__(self, **kwargs):
        super(JPM, self).__init__(**kwargs)
        if self.gateChan is None:
            self.gateChan = LogicalMarkerChannel(label=kwargs['label']+'-gate')
        
class JPMMeasurement(LogicalChannel):
    """docstring for JPMMeasurement"""
    pulseParams = Dict(default={'frequency': 5e6, 'length': .2e-6, 'amp': 1.0, 'shapeFun':PulseShapes.tanh, 'buffer':0.0, 'cutoff':2, 'sigma':1e-9})
    gateChan = Instance((unicode, LogicalMarkerChannel))

    def __init__(self, **kwargs):
        super(JPMMeasurement, self).__init__(**kwargs)
        if self.gateChan is None:
            self.gateChan = LogicalMarkerChannel(label=kwargs['label']+'-gate')

def JPMFactory(label, **kwargs):
    '''Return a saved JPM channel or create a new one. '''
    if Compiler.channelLib and label in Compiler.channelLib and isinstance(Compiler.channelLib[label], JPM):
        return Compiler.channelLib[label]
    else:
        return JPM(label=label, **kwargs)

def JPMMeasFactory(label, **kwargs):
    ''' Return a saved JPMMeasurement channel or create a new one. '''
    if Compiler.channelLib and label in Compiler.channelLib and isinstance(Compiler.channelLib[label], JPMMeasurement):
        return Compiler.channelLib[label]
    else:
        return JPMMeasurement(label=label, **kwargs)