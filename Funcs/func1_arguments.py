#args => all remaining positional arguments
def greeting(name, age=20, *args, **kwargs):
    print(f'name: {name}, \t age: {age}, \t args: {args} \t kwargs: {kwargs}')


greeting('john', 2, [1, 2, 3, 4])
greeting('john', 2, 1, 2, 3, 4)
greeting('john', 2)
greeting('john', 2, weight = 56)