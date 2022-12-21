"""
string.py use for common string operations
https://docs.python.org/3/library/string.html
"""

import string
from string import Formatter, Template


print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)  # ' \t\n\r\x0b\x0c'
print(string.punctuation)


#  the declaration in source code
'''
whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace
'''

'''
__all__ = ["ascii_letters", "ascii_lowercase", "ascii_uppercase", "capwords",
           "digits", "hexdigits", "octdigits", "printable", "punctuation",
           "whitespace", "Formatter", "Template"]
'''
#  The only two classes usable in this library is Formatter and Template
#  and string.capwords(s, sep=None) function, definition is as below
"""
def capwords(s, sep=None):
    return (sep or ' ').join(x.capitalize() for x in s.split(sep))
"""
print(string.capwords('shawn the ship'))  # Shawn The Ship
print(string.capwords('shawn_the_ship', sep='_'))  # Shawn_The_Ship


formatter = Formatter()
msg_1 = formatter.format('{car} is my favorite.', car='BMW')
msg_2 = formatter.format('{} {website}. This is a website for domain '
                         'registration.', 'Welcome to', website='nic.ir')
print(msg_1)
print(msg_2)

msg_3 = '{} {website}. This website is used for domain registration.'.format(
    'Welcome to', website='nic.ir'
)
print(msg_3)

t = Template('Hi my name is $name. love to code $programming_language.'
             ' please have my email address to keep in touch: '
             '$email')
s = t.substitute(name='Amir', programming_language='Python',
                 email='amir.jamshidijam@gmail.com')
print(s)

