import printerm.text2vector
import printerm.vector2gcode
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
print(ser.name)
outline = printerm.text2vector.get_vector_from_char('B')

print(printerm.vector2gcode.get_gcode_from_vector(outline.points, outline.contours))
ser.write(printerm.vector2gcode.get_gcode_from_vector(outline.points, outline.contours))
