import freetype


def get_vector_from_char(character):
    face.load_char(character)
    return face.glyph.outline

face = freetype.Face("Cascadia.ttf")
face.set_char_size(3*4)
