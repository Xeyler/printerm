#include <ft2build.h>
#include FT_FREETYPE_H

#include "text2vector.h"

FT_Library library;
FT_Face face;
int err;

int init(char *filepathname, int face_index) {
	err = FT_Init_FreeType(&library);
	if(err) {
		printf("Error calling FT_Init_FreeType(): %d", err);
		return 1;
	}

	err = FT_New_Face(library, face_index, 0, &face);
	if(err) {
		printf("Error calling FT_New_Face(): %d", err);
		return 1;
	}
	return 0;
}

FT_Outline get_vector_from_char(FT_ULong charcode) {
	int glyph_index = FT_Get_Char_Index(face, charcode);
	if(glyph_index == 0) {
		printf("FT_Get_Char_Index(%lu) returned 0", charcode);
		return null;
	}	
	 // FT_LOAD_DEFAULT looks for bitmap data first. If no bitmap data is found, it loads outline data.
	err = FT_Load_Glyph(face, glyph_index, FT_LOAD_DEFAULT);
	if(err) {
		printf("Error calling FT_Load_Glyph(): %d", err);
		return null;
	}
	return face->glyph->outline;
}
