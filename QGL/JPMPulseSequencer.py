from copy import copy
import numpy as np

from PulseSequencer import PulseBlock

import Channels, PulseShapes, operator

class JPMPulse(object):
    '''
    A single channel pulse object
        label - name of the pulse
        channel - array of jpm/channel objects the pulse acts upon
        shape - numpy array pulse shape
        frameChange - accumulated phase from the pulse
    '''
    def __init__(self, label, channel, shapeParams, amp=1.0, phase=0, frameChange=0):
        self.label = label
        if isinstance(channel, (list, tuple)):
            # with more than one jpm, need to look up the channel
            self.channel = Channels.JPMFactory(reduce(operator.add, [j.label for j in channel]))
        else:
            self.channel = channel
        self.shapeParams = shapeParams
        self.phase = phase
        self.amp = amp
        self.frameChange = frameChange
        self.isTimeAmp = False
        requiredParams = ['length', 'shapeFun']
        for param in requiredParams:
            if param not in shapeParams.keys():
                raise NameError("ShapeParams must incluce {0}".format(param))

    def __repr__(self):
        return str(self)

    def __str__(self):
        if isinstance(self.channel, tuple):
            return '{0}({1})'.format(self.label, ','.join([channel.label for channel in self.channel]))
        else:
            return '{0}({1})'.format(self.label, self.channel.label)

    # adding pulses concatenates the pulse shapes
    def __add__(self, other):
        if self.channel != other.channel:
            raise NameError("Can only concatenate pulses acting on the same channel")
        return CompositePulse([self, other])

    # unary negation inverts the pulse amplitude and frame change
    def __neg__(self):
        shapeParams = copy(self.shapeParams)
        shapeParams['amp'] *= -1
        return JPMPulse(self.label, self.channel, shapeParams, self.phase, -self.frameChange)

    def __mul__(self, other):
        return self.promote()*other.promote()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self == other

    def hashshape(self):
        return hash(frozenset(self.shapeParams.iteritems()))

    def promote(self):
        # promote a Pulse to a PulseBlock
        pb =  PulseBlock()
        pb.pulses = {self.channel: self}
        return pb

    @property
    def length(self):
        return self.shapeParams['length']

    @length.setter
    def length(self, value):
        self.shapeParams['length'] = value
        return value

    @property
    def isZero(self):
        return self.amp == 0

    @property
    def shape(self):
        params = copy(self.shapeParams)
        params['samplingRate'] = self.channel.physChan.samplingRate
        params.pop('shapeFun')
        # params.pop('amp')
        return self.shapeParams['shapeFun'](**params)


def JPMTAPulse(label, channel, length, amp, phase=0, frameChange=0):
    '''
    Creates a time/amplitude pulse with the given pulse length and amplitude
    '''
    params = {'length': length, 'shapeFun': PulseShapes.constant}
    p = JPMPulse(label, channel, params, amp, phase, frameChange)
    p.isTimeAmp = True
    return p

