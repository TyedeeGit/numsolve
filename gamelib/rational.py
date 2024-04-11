"""
Copyright (c) 2024 Tyedee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import math
from abc import abstractmethod
from typing import Union, overload, Any
from numbers import Rational as RationalNumber

Rationalizable = Union['Rational', int, RationalNumber]

class Rational(RationalNumber):
    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __init__(self, n: int, d: int):
        if d < 0:
            n *= -1
            d *= -1
        elif d == 0:
            raise ValueError("Division by 0")
        if math.remainder(n, d) == 0:
            self._numerator = int(n / d)
            self._denominator = 1
        else:
            self._numerator = int(n / math.gcd(n, d))
            self._denominator = int(d / math.gcd(n, d))

    def __abs__(self):
        return Rational(abs(self.numerator), self.denominator)

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    def __add__(self, other: Rationalizable):
        return Rational(self.numerator * self.rationalize(other).denominator + self.rationalize(other).numerator * self.denominator,
                        self.denominator * self.rationalize(other).denominator)

    def __radd__(self, other: Rationalizable):
        return self + other

    def __sub__(self, other: Rationalizable):
        return self + other * -1

    def __rsub__(self, other: Rationalizable):
        return -(self - other)

    def __mul__(self, other: Rationalizable):
        return Rational(self.numerator * self.rationalize(other).numerator, self.denominator * self.rationalize(other).denominator)

    def __rmul__(self, other: Rationalizable):
        return self * self.rationalize(other)

    def __truediv__(self, other: Rationalizable):
        return self * self.rationalize(other).reciprical()

    def __rtruediv__(self, other: Rationalizable):
        return (self / other).reciprical()

    def __floordiv__(self, other: Rationalizable):
        return math.floor(self / self.rationalize(other))

    def __rfloordiv__(self, other: Rationalizable):
        return math.floor(self.rationalize(other) / self)

    def __pow__(self, power, modulo=None):
        return Rational(math.floor(pow(self.numerator, power, modulo)), math.floor(pow(self.denominator, power, modulo)))

    def __rpow__(self, other: Rationalizable):
        return pow(self.rationalize(other), self.numerator/self.denominator)

    def __str__(self):
        if self.denominator == 1:
            num = self.numerator
            strnum = str(num)
            return strnum
        else:
            strnum = f'{self.numerator}/{self.denominator}'
            return strnum

    def __eq__(self, other):
        return self.numerator == self.rationalize(other).numerator and self.denominator == self.rationalize(other).denominator

    def __le__(self, other):
        return self.numerator * self.rationalize(other).denominator <= self.denominator * self.rationalize(other).numerator

    def __lt__(self, other):
        return self.numerator * self.rationalize(other).denominator < self.denominator * self.rationalize(other).numerator

    def __trunc__(self):
        return math.trunc(self.numerator / self.denominator)

    def __floor__(self):
        return math.floor(self.numerator / self.denominator)

    def __ceil__(self):
        return math.ceil(self.numerator / self.denominator)

    def __round__(self, ndigits=None):
        return round(self.numerator / self.denominator, ndigits)

    def __mod__(self, other):
        return (self.numerator / self.denominator) % other

    def __rmod__(self, other):
        return other % (self.numerator / self.denominator)

    def __pos__(self):
        return self

    def __hash__(self):
        return hash((self.numerator, self.denominator))

    def reciprical(self):
        return Rational(self.denominator, self.numerator)

    @classmethod
    def rationalize(cls, number: Rationalizable) -> 'Rational':
        if isinstance(number, Rational):
            return number
        if isinstance(number, int):
            return cls.from_int(number)
        if isinstance(number, RationalNumber):
            return cls.from_other_rational(number)
        raise ValueError('Number should be a rational or int!')

    @classmethod
    def from_int(cls, number: int) -> 'Rational':
        return cls(number, 1)

    @classmethod
    def from_other_rational(cls, number: RationalNumber) -> 'Rational':
        return cls(number.numerator, number.denominator)

def parse(string: str) -> Rational:
    try:
        return Rational(int(string), 1)
    except ValueError:
        split = string.split('/')
        if len(split) != 2:
            raise ValueError('String should be two integers separated by /, or just an integer.')
        return Rational(int(split[0]), int(split[1]))

def main():
    test = parse('3/4')
    print(test)

if __name__ == '__main__':
    main()