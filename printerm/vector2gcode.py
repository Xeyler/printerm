def get_gcode_from_vector(points, contours):
    gcode = ""
    first_point = 0
    for number_of_points_in_contour in contours:
        for i in range(first_point, number_of_points_in_contour):
            x = points[i][0] + 150
            y = points[i][1] + 100

            gcode += "G1X" + str(x) + "Y" + str(y) + '\n'

            if i is 0:
                gcode += "G1Z1\n"
        gcode += "G1Z5\n"

    return gcode
