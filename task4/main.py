import sys


def read_file(path: str) -> list[int]:
    with open(path) as file:
        content = list(map(int, file.read().strip().split("\n")))
    return content


def get_median(values: list[int]) -> int:
    return sorted(values)[len(values) // 2]


def main(values: list[int]):
    median = get_median(values)
    turns = sum((abs(median - val) for val in values))
    if turns > 20:
        print(
            "20 ходов недостаточно для приведения всех элементов массива к одному числу"
        )
    else:
        print(turns)


if __name__ == "__main__":
    file_path = sys.argv[1]
    values = read_file(file_path)
    main(values)
