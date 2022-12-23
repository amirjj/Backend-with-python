#totally mutable
list_test = []
list_test = list()

#set is mutable itself so you can add and pop from it, but set elements are immuatable so you can't 
#change one of its items
set_test = {} #interpreter translate empty braces as dictionary so better to use set() when you are
#going to define empty set
set_test = set()

#tuple is completely immuatble, you can't add/ pop from it. you can't change elements also
tuple_test = ()
tuple_test = tuple()

dict_test = {}
dict_test = dict()
dict_test = dict(name="john", age=20, weight=56.4)
dict_test.keys()
dict_test.values()
dict_test["name"]
dict_test["fullname"]
dict_test.get("fullname")
dict_test.get("name")
dict_test.setdefault("height", 180)
print(dict_test)
dict_test.get("family", "bernard")
new_dict = {"city": "NewYork"}
dict_test.update(new_dict)
del dict_test['city']
all_dict = {**dict_test, **new_dict} #dict_test & new_dict will not change
wierd_dict = {1: "one", 1.5: "float", ("john","doe"): "What?"}
wierd_dict.get(('john', 'doe'))


a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
a == b == c == d == e == f
id(a) == id(b)
