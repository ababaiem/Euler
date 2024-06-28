
def resolve() -> int:

    predicate = lambda i: i % 3 == 0 or i % 5 == 0

    naturals = range(1, 1000)

    multiples = filter(predicate, naturals)

    return sum(multiples)


if __name__ == "__main__":

    print(resolve())

