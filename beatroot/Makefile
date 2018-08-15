.PHONY: all

all: BeatRoot.jar

bin:
	mkdir bin

%/BeatRoot.class: bin
	javac -d bin at/ofai/music/beatroot/BeatRoot.java
	cp -r audio bin

BeatRoot.jar: bin/at/ofai/music/beatroot/BeatRoot.class
	jar -cvfm BeatRoot.jar META-INF/MANIFEST.MF -C bin .
	cp $@ ../m2/beatroot
