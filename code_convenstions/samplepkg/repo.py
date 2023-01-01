
_single_underscore_var = 150

other_var = 200


def _single_underscore_func():
    print('_single_underscore_func')


__double_underscore_var = 300


def __double_underscore_func():
    print('__double_underscore_func')


"""
Sometimes the most fitting name for a variable is already taken by a keyword. 
Therefore names like class or def cannot be used as variable names in Python
"""
var_ = 200


def class_():
    print('class_')


if __name__ == '__main__':
    # below underscore attrs are available in module
    print(_single_underscore_var)
    _single_underscore_func()

    print(__double_underscore_var)
    __double_underscore_func()


"""
__var
This is also called name mangling—the interpreter changes the name of the 
variable in a way that makes it harder to create collisions when the class is 
extended later.
A double underscore prefix causes the Python interpreter to rewrite the 
attribute name in order to avoid naming conflicts in subclasses.


class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23
        
>>> t = Test()
>>> dir(t)
['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', '_bar', 'foo']

https://dbader.org/blog/meaning-of-underscores-in-python
"""
