import sys


def read_circle(file_path):
    """
    Reads the coordinates of the circle centr and radius from a file
    return a tuple (x, y, r)
    """

    with open(file_path, "r") as file:
        x, y = map(float, file.readline().strip().split())
        r = float(file.readline().strip())
    return x, y, r


def read_points(file_path):
    """
    Reads coordinates of points from a file
    return list of tuples [(x1, y1), (x2, y2), (x3, y3)]
    """

    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points


def determine_position(circle, point):
    """
    Determines the position as well.
    return:
    0 - point on the circle.
    1 - point inside the circle.
    2 - point outside the circle.
    """
    x_c, y_c, r = circle
    x, y = point
    distance_squared = (x - x_c) ** 2 + (y - y_c) ** 2
    radius_squared = r**2

    if distance_squared == radius_squared:
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2


def main(circle_file, points_file):
    circle = read_circle(circle_file)
    points = read_points(points_file)

    for point in points:
        position = determine_position(circle, point)
        print(position)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("'Use: python task2.py <circle_file> <points_file>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    main(circle_file, points_file)
