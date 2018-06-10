import unittest

if '__builtin__' not in dir() or not hasattr(__builtin__, 'profile') or \
        'profile' not in dir():

    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner


@profile
def some_fn(nbr):
    return nbr * 2


class TestCase(unittest.TestCase):
    def test(self):
        result = some_fn(2)
        self.assertEquals(result, 4)
