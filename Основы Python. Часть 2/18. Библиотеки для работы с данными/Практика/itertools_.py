 
import itertools

if __name__ == '__main__':
    colors = ["красный", "зелёный", "жёлтый", "чёрный", "белый"]

    for item in itertools.permutations(colors, 4):
        print(item)

    print("-" * 20)

    for item in itertools.combinations(colors, 4):
        print(item)

    print("-" * 20)

    c =  itertools.cycle(["1", "2", "3"])
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))

    print("-" * 20)

