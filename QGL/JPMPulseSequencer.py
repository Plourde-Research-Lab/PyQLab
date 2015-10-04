from copy import copy
import numpy as np

from PulseSequencer import PulseBlock

class JPMPulse(object):
    '''
    A single channel pulse object
        label - name of the pulse
        jpms - array of jpm/channel objects the pulse acts upon
        shape - numpy array pulse shape
        frameChange - accumulated phase from the pulse
    '''
    def __init__(self, label, jpms, shapeParams, phase=0, frameChange=0):
        self.label = label
        if isinstance(jpms, (list, tuple)):
            # with more than one jpm, need to look up the channel
            self.jpms = Channels.JPMFactory(reduce(operator.add, [j.label for j in jpms]))
        else:
            self.jpms = jpms
        self.shapeParams = shapeParams
        self.phase = phase
        self.frameChange = frameChange
        self.isTimeAmp = False
        requiredParams = ['amp', 'length', 'shapeFun']
        for param in requiredParams:
            if param not in shapeParams.keys():
                raise NameError("ShapeParams must incluce {0}".format(param))

    def __repr__(self):
        return str(self)

    def __str__(self):
        if isinstance(self.jpms, tuple):
            return '{0}({1})'.format(self.label, ','.join([jpm.label for jpm in self.jpms]))
        else:
            return '{0}({1})'.format(self.label, self.jpms.label)

    # adding pulses concatenates the pulse shapes
    def __add__(self, other):
        if self.jpms != other.jpms:
            raise NameError("Can only concatenate pulses acting on the same channel")
        return CompositePulse([self, other])

    # unary negation inverts the pulse amplitude and frame change
    def __neg__(self):
        shapeParams = copy(self.shapeParams)
        shapeParams['amp'] *= -1
        return Pulse(self.label, self.jpms, shapeParams, self.phase, -self.frameChange)

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
        pb.pulses = {self.jpms: self}
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
        return self.shapeParams['amp'] == 0 or np.all(self.shape == 0)

    @property
    def shape(self):
        params = copy(self.shapeParams)
        params['samplingRate'] = self.jpms.physChan.samplingRate
        params.pop('shapeFun')
        params.pop('amp')
        return self.shapeParams['shapeFun'](**params)


def JPMTAPulse(label, jpms, length, amp, phase=0, frameChange=0):
    '''
    Creates a time/amplitude pulse with the given pulse length and amplitude
    '''
    params = {'amp': amp, 'length': length, 'shapeFun': PulseShapes.constant}
    p = JPMPulse(label, jpms, params, phase, frameChange)
    p.isTimeAmp = True
    return p

