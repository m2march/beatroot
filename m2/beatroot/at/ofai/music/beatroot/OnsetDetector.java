package at.ofai.music.beatroot;

import at.ofai.music.beatroot.AudioProcessor;
import at.ofai.music.util.Event;
import java.util.Iterator;


public class OnsetDetector {

    public static void main(String argv[]) {
        if (argv.length < 1) {
            System.out.println("Usage: OnsetDetector audio_file");
            System.exit(0);
        }
        System.out.println("> Reading file: " + argv[0]);
        AudioProcessor audioProcessor = new AudioProcessor();
        audioProcessor.setInputFile(argv[0]);
        audioProcessor.processFile();
        audioProcessor.findOnsets(0.35, 0.84);
        Iterator<Event> it = audioProcessor.onsetList.iterator();
        System.out.println("> Calculated " + audioProcessor.onsetList.size() +
                           " onsets.");
        while (it.hasNext()) {
            System.out.println(it.next().keyDown);
        }
    }

}
