#ifndef text2vector
#define text2vector

int init(char *filepathname, int face_index);

FT_Outline get_vector_from_char(FT_ULong charcode);

#endif
