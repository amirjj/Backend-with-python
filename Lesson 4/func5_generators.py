
# # return value (the list) will be calculated and returned and done (function runtime finished)
# def filter_number():
#     # return [i for i in range(100) if i % 7 == 0]
#     tmp = list()
#     for i in range(100):
#         if i % 7 == 0:
#             tmp.append(i)
#     #function finishes as soon as value returned all at once
#     print("regular function finished now")
#     return tmp

# filter_number_regular_function = filter_number()
# for num in filter_number_regular_function:
#     print(num)


def filter_number_generator():
    for i in range(100):
        if i % 7 == 0:
            yield i
    print("generator function finished now")

# print(filter_number_generator())
# lifetime of above generator function is related for below loop
# untill below loop nothing happen in above generator and nothing will be returned till then
filter_generator_function = filter_number_generator()
for num in filter_generator_function:
    print(num)


a = [i for i in range(5)]
print(type(a))
b = (i for i in range(5))
print(b)

print(type(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
# print(next(b)) #StopIteration
print(b)

"""
downside of generators:
-you don't have the length, you just have the next item
-you don't know when you will be in the end
-when you reach the last item in generator with next() or for, the generator is done,
    you can't use it again

benefits:
-low resource allocation (Memory efficient)
"""


