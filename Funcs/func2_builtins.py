#built-in functions
#https://docs.python.org/3/library/functions.html
# all()
a = [True, True, True]
all(a)
a.append(False)
all(a)
a = [1, 2, 3, 4, 0]
all(a)
bool(0)
any(a)

msg = "Hello World!"
ascii(msg)
bin(3)
oct(30)
hex(30)
bool(1==2)

callable(msg)

def test():
    pass

callable(test)

chr(97)
ord('a')

#create asd file 
compile()

divmod(13, 3)

a = ['a', 'b', 'c', 'd']
for index, value in enumerate(a):
    print(index, value)

a = dict(name = "john", family = 'doe', age = 13)
for i, v in enumerate(a):
    print(i, v)
    print(i, v, a[v])

eval('2+3')
c = "[(i, v) for i, v in enumerate(a)]"
eval(c)

a = [1 ,2 ,3 ,3 ,4 ,4]
user_set = set(a)
frozen = frozenset(a)
user_set.add(15)
frozen.add(15)

#just show global variabls not those in functions
globals()

help()
#local symbol table
locals()

a = [1, 2, 3, 4]
a.reverse()
a.reverse()
for i in reversed(a):
    print(i)
print(a)

a = [1 ,2 ,10 ,5 , 3]
for i in sorted(a):
    print(i)
print(a)

