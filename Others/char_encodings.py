"""
ASCII was the most common character encoding on the World Wide Web until
December 2007, when UTF-8 encoding surpassed it; UTF-8 is backward
compatible with ASCII
"""


def print_asciis():
    for i in range(2000):
        print(f'For {i}, ASCII: {chr(i)}, UTF-8 (URL Encode): '
              f'{chr(i).encode("utf-8")}')


if __name__ == '__main__':
    print_asciis()

