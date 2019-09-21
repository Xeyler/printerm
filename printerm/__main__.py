import printerm.text2vector
import printerm.vector2gcode
import serial

outline = printerm.text2vector.get_vector_from_char('B')

codes = printerm.vector2gcode.get_gcode_from_vector(outline.points, outline.contours)
print(codes)
printerm.vector2gcode.send_codes_to_printer(codes)
