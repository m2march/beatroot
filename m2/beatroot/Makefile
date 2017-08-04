.PHONY: all

all: BeatRoot.jar


BeatRoot.jar: bin/at/ofai/music/beatroot/BeatRoot.class
	jar -cfm BeatRoot.jar META-INF/MANIFEST.MF -C bin .

%/BeatRoot.class: bin
	javac -d bin at/ofai/music/beatroot/BeatRoot.java

bin:
	mkdir bin
