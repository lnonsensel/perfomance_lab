import sys


def read_file_dots(path: str) -> list[tuple[int]]:
    dots = []
    with open(path) as file:
        content = file.read().strip().split("\n")
        for row in content:
            dots.append(tuple(map(int, row.split())))
    return dots


def F(x, x0, y, y0, a, b) -> int | float:
    return ((x - x0) / a) ** 2 + ((y - y0) / b) ** 2


def main(cent: tuple, rad: tuple, dots: list[tuple]) -> None:
    x0, y0 = cent
    a, b = rad
    for dot in dots:
        x, y = dot
        f_value = F(x, x0, y, y0, a, b)
        if f_value < 1:
            print(1)
        elif f_value > 1:
            print(2)
        else:
            print(0)


if __name__ == "__main__":
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    cent, rad = read_file_dots(file1_path)
    dots = read_file_dots(file2_path)
    main(cent, rad, dots)
