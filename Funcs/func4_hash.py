"""
All immutable objects are hashable, but not all hashable objects are immutable.

Immutable objects are a type of object that cannot be modified after they were created. 
Hashable objects, on the other hand, are a type of object that you can call hash() on.
"""

my_list = [1, 2, 3, 4]
hash(my_list())
#lists are not hashable
#just a hashable parameter can be used as dictinary key cause need to be used in hash table
my_dict = {my_list: "test"}

a = 10
b = 10

hash(a) == hash(b)

b = 10.0
hash(a) == hash(b)

my_set = {1, 2, 3}
type(my_set)

hash(my_set)
my_dict = {my_set: "foe"}

my_tuple = (1 ,2 ,3)
hash(my_tuple)
my_dict = {my_tuple: "foe"}
