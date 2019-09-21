import serial
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/ttyUSB0', 115200)

def get_gcode_from_vector(points, contours):
    arr = [];

    gcode = []
    first_point = 0
    for number_of_points_in_contour in contours:
        for i in range(first_point, number_of_points_in_contour + 1):
            x = points[i][0] + 100
            y = points[i][1] + 100

            arr.append((x, y))

            gcode.append("G1X" + str(x) + "Y" + str(y))

            if i is first_point:
                gcode.append("G1Z1")
        arr.append((points[first_point][0] + 100, points[first_point][1] + 100))
        gcode.append("G1X" + str(points[first_point][0] + 100) + "Y" + str(points[first_point][1] + 100))
        first_point = number_of_points_in_contour + 1
        gcode.append("G1Z5")

        print(arr)

        plt.plot(*zip(*arr))
        arr = []

    plt.show()

    return gcode

def send_codes_to_printer(codes):
    for code in codes:
        ser.write((code + '\n').encode())
        while True:
            result = ser.readline()
            print(result)
            if result == b"ok\n":
                break
