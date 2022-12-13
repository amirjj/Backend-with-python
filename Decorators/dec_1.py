

def logger(func):
    """
    This is a sample decorator
    :param func: the function which is going to be wrapped (decorated)
    :return: return the wrapper function pointer
    """
    def wrapped_func(*args, **kwargs):
        print(args, kwargs)
        return func(*args, **kwargs)
    return wrapped_func  # returning the pointer to the function


@logger
def pow2(num):
    return num ** 2


if __name__ == "__main__":
    print(pow2(10))

