# -*- coding: utf-8 -*-

from math import sqrt

__author__ = 'fyabc'


class Vector2:
    """A class for 2d vector.
    Values of this vector are float.
    """
    __slots__ = ('_v', )

    def __init__(self, x=0., y=0.):
        if hasattr(x, '__getitem__'):
            x, y = x
        self._v = [float(x), float(y)]

    @classmethod
    def fromFloats(cls, x, y):
        vec = cls.__new__(cls)
        vec._v = [x, y]
        return vec

    @classmethod
    def fromIter(cls, iterable):
        iterable = iter(iterable)
        vec = cls.__new__(cls)
        vec._v = [float(next(iterable)), float(next(iterable))]
        return vec

    @classmethod
    def from2Point(cls, p1, p2):
        vec = cls.__new__(cls)
        x1, y1 = p1
        x2, y2 = p2
        vec._v = [float(x2 - x1), float(y2 - y1)]
        return vec

    def copy(self):
        vec = self.__new__(self.__class__)
        vec._v = self._v[:]
        return vec

    # Hook methods.

    def __str__(self):
        x, y = self._v
        return '(%f, %f)' % (x, y)

    def __repr__(self):
        x, y = self._v
        return 'Vector2(%f, %f)' % (x, y)

    def __iter__(self):
        return self._v.__iter__()

    def __len__(self):
        return 2

    def __getitem__(self, item):
        try:
            return self._v[item]
        except IndexError:
            raise IndexError("There are 2 values in this object, index should be 0 or 1")

    def __setitem__(self, key, value):
        try:
            self._v[key] = 1.0 * value
        except IndexError:
            raise IndexError("There are 2 values in this object, index should be 0 or 1!")
        except TypeError:
            raise TypeError("Must be a number")

    def __eq__(self, other):
        x, y = self._v
        x2, y2 = other
        return x == x2 and y == y2

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self._v)

    def __add__(self, other):
        x, y = self._v
        x2, y2 = other
        return Vector2.fromFloats(x + x2, y + y2)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        x2, y2 = other
        self._v[0] += x2
        self._v[1] += y2
        return self

    def __sub__(self, other):
        x, y = self._v
        x2, y2 = other
        return Vector2.fromFloats(x - x2, y - y2)

    def __rsub__(self, other):
        x, y = self._v
        x2, y2 = other
        return self.fromFloats(x2 - x, y2 - y)

    def __isub__(self, other):
        x2, y2 = other
        self._v[0] -= x2
        self._v[1] -= y2
        return self

    def __mul__(self, other):
        """If other is a vector, return inner product, else return a vector."""
        x, y = self._v
        if hasattr(other, '__getitem__'):
            x2, y2 = other
            return x * x2 + y * y2
        else:
            return Vector2.fromFloats(x * other, y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        self._v[0] *= other
        self._v[1] *= other
        return self

    def __truediv__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __itruediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __neg__(self):
        x, y = self._v
        return Vector2.fromFloats(-x, -y)

    def __pos__(self):
        return self.copy()

    def __bool__(self):
        x, y = self._v
        return bool(x or y)

    def __abs__(self):
        x, y = self._v
        return Vector2.fromFloats(abs(x), abs(y))

    @property
    def length(self):
        """Length of the vector."""
        x, y = self._v
        return sqrt(x * x + y * y)

    @length.setter
    def length(self, newLength):
        v = self._v
        try:
            l = newLength / self.length
        except ZeroDivisionError:
            v[0], v[1] = 0.0, 0.0
            return
        v[0] *= l
        v[1] *= l

    @property
    def x(self):
        """x component."""
        return self._v[0]

    @x.setter
    def x(self, newX):
        try:
            self._v[0] = 1.0 * newX
        except:
            raise TypeError("Must be a number")

    @property
    def y(self):
        """x component."""
        return self._v[1]

    @y.setter
    def y(self, newX):
        try:
            self._v[1] = 1.0 * newX
        except:
            raise TypeError("Must be a number")

    def normalize(self):
        self.length = 1.
        return self

    def getNormalized(self):
        vec = self.copy()
        vec.length = 1.
        return vec

    def distance(self, other):
        x, y = self._v
        x2, y2 = other
        return sqrt((x2 - x) ** 2 + (y2 - y) ** 2)


def test():
    v = Vector2(3, 5)
    print(v)
    print(v.length)
    v.length = 4
    print(v.length)
    print(v)
    v.normalize()
    print(v)


if __name__ == '__main__':
    test()
