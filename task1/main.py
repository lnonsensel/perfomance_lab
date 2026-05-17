import threading
import sys


def main(n: int | None = None, m: int | None = None) -> None:
    n = int(input()) if n is None else n
    m = int(input()) if m is None else m
    m -= 1
    i = 1
    while True:
        print(i if i != 0 else n, end="")
        i += m
        i %= n
        if i == 1:
            return


if __name__ == "__main__":
    n1 = int(sys.argv[1])
    m1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    m2 = int(sys.argv[4])

    t1 = threading.Thread(
        target=main,
        args=(
            n1,
            m1,
        ),
    )
    t2 = threading.Thread(
        target=main,
        args=(
            n2,
            m2,
        ),
    )
    t1.start()
    t2.start()
    t1.join()
    t2.join()
