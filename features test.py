def plus_set(a: tuple, b: tuple):
    a = list(a)
    b = list(b)
    return a[0] + b[0], a[1] + b[1]


print(plus_set((1, 2), (2, 1)))
