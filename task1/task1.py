import sys

def circular_path(n, m):
    """Traversing an array of numbers in a circle with a given step"""

    buffer = list(range(1, n + 1))
    index = 0
    path = []

    while len(path) < n:
        path.append(buffer[index])
        index = (index + m - 1) % n
    return path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Use: python task1.py <n> <m>')
        sys.argv(1)

    n, m = int(sys.argv[1]),int(sys.argv[2])
    path = circular_path(n, m)
    print(''.join(map(str, path)))