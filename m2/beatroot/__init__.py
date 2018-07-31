import pkg_resources
from subprocess import Popen

JAR_FILE_0_5_6 = pkg_resources.resource_filename(__name__, 'BeatRoot.jar')
JAR_FILE_0_5_8 = pkg_resources.resource_filename(__name__, 
                                                 'beatroot-0.5.8.jar')

version_map = {
    '0.5.6': JAR_FILE_0_5_6,
    '0.5.8': JAR_FILE_0_5_8,
}

def beatroot(audio_file, onsets=False, output=None, version='0.5.6'):
    '''
    Args:
        audio_file: path to audio file to analyze
        onsets: whether to output onset information
        output: if not None, write output to given path
    '''
    args = ['java', '-jar', version_map[version]]
    if onsets:
        args.append('-O')

    _output = 'temp.out' if output is None else output

    args.extend(['-o', _output])
    args.append(audio_file)

    p = Popen(args)
    p.communicate()
    if output is None:
        with open(_output, 'r') as f:
            beats = [float(l) for l in f]
            return beats
        os.remove(_output)
