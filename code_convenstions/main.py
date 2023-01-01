"""
Single Leading Underscore: _var
Single Trailing Underscore: var_
Double Leading Underscore: __var
Double Leading and Trailing Underscore: __var__
Single Underscore: _
"""


def test_first_repo():
    # importing _underscore is just possible specifically mentioning
    # just warning will be raised
    from samplepkg.repo import _single_underscore_var, _single_underscore_func,\
        __double_underscore_var, __double_underscore_func

    # importing _underscore attr with * will not import
    # from samplepkg.repo import *

    print(other_var)
    print(_single_underscore_var)
    _single_underscore_func()

    print(__double_underscore_var)
    __double_underscore_func()


def test_second_repo():
    from anotherpkg.newrepo import A

    a = A()
    print(a._underscore_class_var)
    a._under_score_method()

    print(a.__double_underscore_class_var)
    a.__double_under_score_method()  # Error


if __name__ == '__main__':
    test_second_repo()
