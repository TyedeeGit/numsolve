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

class Rational:
    def __init__(self, n, d):
        if d < 0:
            n *= -1
            d *= -1
        elif d == 0:
            raise ValueError("Division by 0")
        if math.remainder(n, d) == 0:
            self.numerator = int(n / d)
            self.denominator = 1
        else:
            self.numerator = int(n / math.gcd(n, d))
            self.denominator = int(d / math.gcd(n, d))

    def __abs__(self):
        return Rational(abs(self.numerator), self.denominator)

    def __add__(self, other):
        if type(other) is int:
            return Rational(other * self.denominator + self.numerator, self.denominator)
        else:
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)

    def __sub__(self, other):
        return self + other * -1

    def __mul__(self, other):
        if type(other) is int:
            return Rational(other * self.numerator, self.denominator)
        else:
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __str__(self):
        if self.denominator == 1:
            num = self.numerator
            strnum = str(num)
            return strnum
        else:
            strnum = f'{self.numerator}/{self.denominator}'
            return strnum

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def reciprical(self):
        return Rational(self.denominator, self.numerator)

def parse(string: str) -> Rational:
    split = string.split('/')
    if len(split) != 2:
        raise ValueError('String should be two integers separated by /')
    return Rational(int(split[0]), int(split[1]))

def main():
    test = parse('3/4')
    print(test)

if __name__ == '__main__':
    main()