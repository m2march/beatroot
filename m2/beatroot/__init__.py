import pkg_resources
import math
import tempfile
import os

import numpy as np

from scipy.io import wavfile
from subprocess import Popen
from typing import *

JAR_FILE_0_5_6 = pkg_resources.resource_filename(__name__, 'BeatRoot.jar')
JAR_FILE_0_5_8 = pkg_resources.resource_filename(__name__, 
                                                 'beatroot-0.5.8.jar')

version_map = {
    '0.5.6': JAR_FILE_0_5_6,
    '0.5.8': JAR_FILE_0_5_8,
}

SR = 44100

class BeatrootInput:
    '''
    Returns a filename to an audio file to input beatroot.

    It can be initiated with the filename of a already existing audio file
    or a list of onset times (in seconds). In the latter case, the input is
    transformed into an audio file that can be used by beatroot. 

    This temp file is deleted upon exit.
    '''

    def __init__(self, input: Union[str, List[float]]):
        '''
        Returns a filename to an audio file.

        Args:
            input (as str): filename of an audio file
            input (as list of floats): onset times (in seconds)
        '''
        self.temp = None

        if isinstance(input, str):
            return input
        
        top = math.ceil(max(input))
        if (top == max(input)):
            top += 1

        signal = np.zeros(SR * top)
        for o in input:
            signal[int(o * SR)] = 1

        h, self.temp = tempfile.mkstemp()
        wavfile.write(self.temp, SR, signal)

    def __enter__(self):
        return self.temp

    def __exit__(self, type, value, traceback):
        if self.temp is not None:
            os.remove(self.temp)


def beatroot(input, onsets=False, output=None, version='0.5.6'):
    '''
    Args:
        input: list of onset times (in seconds) or path to audio file to analyze
        onsets: whether to output onset information
        output: if not None, write output to given path
    '''
    args = ['java', '-jar', version_map[version]]
    if onsets:
        args.append('-O')

    _output = 'temp.out' if output is None else output

    args.extend(['-o', _output])

    with BeatrootInput(input) as audio_file:
        args.append(audio_file)

        p = Popen(args)
        p.communicate()
        if output is None:
            with open(_output, 'r') as f:
                beats = [float(l) for l in f]
                return beats
            os.remove(_output)
