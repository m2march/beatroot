import pkg_resources
from subprocess import Popen

JAR_FILE = pkg_resources.resource_filename(__name__, 'BeatRoot.jar')

def beatroot(audio_file, onsets=False, output=None):
    '''
    Args:
        audio_file: path to audio file to analyze
        onsets: whether to output onset information
        output: if not None, write output to given path
    '''
    args = ['java', '-jar', JAR_FILE]
    if onsets:
        args.append('-O')

    _output = 'temp.out' if output is None else output

    args.extend(['-o', _output])
    args.append(audio_file)

    p = Popen(args)
    p.communicate()
    if output is None:
        with open(_output, 'r') as f:
            for l in f:
                sys.stdout.write(l)
        os.remove(_output)
