bin/printerm:
	mkdir -p bin
	gcc -o bin/printerm $(shell pkg-config --cflags freetype2) src/text2vector.c src/main.c $(shell pkg-config --libs --static freetype2)

clean:
	rm -rf bin/
