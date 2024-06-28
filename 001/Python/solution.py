
def resolve() -> int:

    _sum: int = 0

    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            _sum += i

    return _sum

if __name__ == "__main__":

    print(resolve())

