from functools import partial


def multiply(x, y, z):
    return x * y * z


par_func = partial(multiply, 4, 5)
# partial(func, *args, **keywords)

print(par_func(3))
