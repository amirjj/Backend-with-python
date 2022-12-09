# map(<function>, <iterable>)
# filter(<funtion returning bool>, <iterable>)
# lambda <input 1>, <input 2> , ..., <input n> : <output>

"""
Note that filter(function, iterable) is equivalent to the generator expression 
(item for item in iterable if function(item)) if function is not None 
and (item for item in iterable if item) if function is None.
"""

a = [0 ,1 ,2 ,3 ,4 ]
list(filter(None, a))

b = [True, False, True, True]
list(filter(None, b))


