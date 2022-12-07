
number_list = [i for i in range(100)]
number_list = [i for i in range(1, 50, 3)]
odd_list = [i for i in range(1, 50, 3) if i % 2 != 0]
print(odd_list)

tmp = [ i for i in range(10)]
print(type(tmp))
tmp = {i for i in range(10)}
print(type(tmp))
tmp = (i for i in range(10))
print(type(tmp))