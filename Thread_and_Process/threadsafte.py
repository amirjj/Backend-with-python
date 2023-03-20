import sys


def test():
	names = []
	print(sys.getrefcount(names))


print(sys.getrefcount(names))
"""
this will raise an error cuase after the scope of test finished, names will be purged by interpreter.
This code is not threadsafe as if two thread run this code after purging names variable in first thread,
the second thread can not access it too cause threads uses sharedmemory
"""


if __name__ == '__main__':
	test()
