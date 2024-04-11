"""
Copyright (c) 2024 Ammar Abbas

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

from typing import Optional
from abc import ABC, abstractmethod


class Series(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def evaluate(self) -> Optional[float]:
        pass


class GeometricSeries(Series):
    def __init__(self, starting_value, ratio):
        self.starting_value = starting_value
        self.ratio = ratio

    def __str__(self):
        return f'{self.starting_value} + {self.starting_value*self.ratio} + {self.starting_value*self.ratio**2} + ...'

    def evaluate(self) -> Optional[float]:
        if self.ratio >= 1:
            return None
        return self.starting_value/(1 - self.ratio)


def main():
    series = GeometricSeries(2, 1/8)
    print(series)
    print(round(series.evaluate(), 2))


if __name__ == '__main__':
    main()
