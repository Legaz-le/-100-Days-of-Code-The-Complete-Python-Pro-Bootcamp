from statistics import multimode


def add(*hard):
    sum = 0
    for n in hard:
        sum += n
    return sum

# print(add(3,5,6,4,8,8,9,1,2))

def calculater(n, **next):
    print(next)
    # for key, value in next.items():
    #     print(key)
    #     print(value)

    # print(next["add"])
    n += next["add"]
    n *= next["multiply"]
    print(n)





calculater(2, add= 3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
