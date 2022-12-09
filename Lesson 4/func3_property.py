
class C:
    def __init__(self):
        self._x = None

    def set_x(self, val):
        self._x = val
    
    def get_x(self):
        return self._x

    def del_x(self):
        del self._x

c = C()
c.set_x(1)
# print(c.x) #'C' object has no attribute 'x'
print(c.get_x())
c.set_x(2)
print(c.get_x())
# c.del_x()
# print(c.get_x())


class D:
    def __init__(self):
        self._x = None

    def set_x(self, val):
        self._x = val
    
    def get_x(self):
        return self._x

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "This is x property")

d = D()
d.x = 1
print(d.x)
print(help(d))


#Another way?

class E:
    def __init__(self) -> None:
        self._x = None

    @property
    def x(self):
        """ This is x property"""
        return self._x
    
    @x.setter
    def x(self, val):
        self._x = val
    
    @x.deleter
    def x(self):
        del self._x


e = E()

print("vars---------")
print(vars(e))
print("dir---------")
print(dir(e))
e.x = 10
print(e.x)
del e.x