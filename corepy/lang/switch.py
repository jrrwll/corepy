# http://code.activestate.com/recipes/410692/

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


# break is used here to look as much like the real thing as possible, but
# elif is generally just as good and more concise.

# Empty suites are considered syntax errors, so intentional fall-throughs
# should contain 'pass'
c = 'z'
for case in switch(c):
    if case('a'): pass  # only necessary if the rest of the suite is empty
    # ...
    if case('z'):
        print("c is lowercase!")
        break
    if case('A'): pass
    # ...
    if case('Z'):
        print("c is uppercase!")
        break
    if case():  # default
        print("I don't know what c was!")

# As suggested by Pierre Quentel, you can even expand upon the
# functionality of the classic 'case' statement by matching multiple
# cases in a single shot. This greatly benefits operations such as the
# uppercase/lowercase example above:
import string

c = 'A'
for case in switch(c):
    if case(*string.ascii_lowercase):  # note the * for unpacking as arguments
        print("c is lowercase!")
        break
    if case(*string.ascii_uppercase):
        print("c is uppercase!")
        break
    if case('!', '?', '.'):  # normal argument passing style also applies
        print("c is a sentence terminator!")
        break
    if case():  # default
        print("I don't know what c was!")
