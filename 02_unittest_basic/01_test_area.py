import unittest

def area(width, height):
    """Function returns the area of the  rectangle"""

    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive')

    return width * height

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20)


if __name__ == '__main__':
    unittest.main(verbosity=2)
