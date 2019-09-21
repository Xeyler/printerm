#include <ft2build.h>
#include FT_FREETYPE_H

#include <stdio.h>
#include "text2vector.h"

int main(void) {
	init("mononoki_regular.ttf", 0);
	get_vector_from_char(0);
	printf("done");
	return 0;
}
