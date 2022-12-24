"""
ASCII was the most common character encoding on the World Wide Web until
December 2007, when UTF-8 encoding surpassed it; UTF-8 is backward
compatible with ASCII
"""

"""
URL encoding converts characters into a format that can be transmitted over the 
Internet.

URLs can only be sent over the Internet using the ASCII character-set.
Since URLs often contain characters outside the ASCII set, the URL has to be 
converted into a valid ASCII format.
URL encoding replaces unsafe ASCII characters with a "%" followed by two 
hexadecimal digits.
URLs cannot contain spaces. URL encoding normally replaces a space with a 
plus (+) sign or with %20.


"""

def print_asciis():
    for i in range(2000):
        print(f'For {i}, ASCII: {chr(i)}, UTF-8 (URL Encode): '
              f'{chr(i).encode("utf-8")}')


if __name__ == '__main__':
    print_asciis()

