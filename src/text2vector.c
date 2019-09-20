#include <ft2build.h>
#include FT_FREETYPE_H

FT_Library library;
FT_Face face;
int err;

int init(char *filepathname, int face_index) {
	err = FT_Init_FreeType(&library);
	if(err) {
		printf("Error calling FT_Init_FreeType(): %d", err);
	}

	err = FT_New_Face(library, face_index, 0, &face);
	if(err) {
		printf("Error calling FT_New_Face(): %d", err);
	}
}
