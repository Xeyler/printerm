bin/printerm:
	gcc $(shell pkg-config --cflags freetype2) src/text2vector.c src/main.c
