from math import comb
import random
from typing import Type, Callable


def simplex(n: int, dim: int):
    return comb(n + dim - 1, dim)


class Polynomial:
    terms_cache = {}

    def __init__(self, degree: int, variables: int, coefficients: list[list[int, ...], ...]):
        """
        Initializes a Polynomial object.
        """
        self.degree = degree
        self.variables = variables
        if len(coefficients) != len(self.terms):
            raise ValueError(f'Expected {len(self.terms)} coefficients(s), got {len(coefficients)}.')
        self.coefficients = coefficients

    def __str__(self):
        output = ''
        for i, (term, coefficient) in enumerate(zip(self.terms, self.coefficients)):
            if coefficient:
                if i:
                    output += ' + ' if coefficient > 0 else ' - '
                output += str(abs(coefficient))
                for var in term:
                    if var:
                        output += f'*x{var}'
        return output

    def evaluate(self, *values: int) -> int:
        """
        Evaluates the polynomial at the given values.
        :param values:
        :return:
        """
        output = 0
        if len(values) != self.variables:
            raise ValueError(f'Expected {self.variables} value(s), got {len(values)}.')
        for i, term in enumerate(self.terms):
            term_value = self.coefficients[i]
            for var in term:
                if var:
                    term_value *= values[var - 1]
            output += term_value
        return output

    @property
    def terms(self) -> list[int, ...]:
        """
        Gets the variables for the terms of the polynomial.
        :return:
        """
        if not self.terms_cache.get(self.variables, None):
            self.terms_cache[self.variables] = [[[]]]
        if len(self.terms_cache[self.variables]) - 1 >= self.degree:
            return self.terms_cache[self.variables][self.degree]
        for i in range(len(self.terms_cache[self.variables]) - 1, self.degree):
            prev_terms = self.terms_cache[self.variables][-1]
            new_terms = []
            for variable in range(self.variables + 1):
                for term in prev_terms[:simplex(variable + 1, i)]:
                    new_terms.append([self.variables - variable])
                    new_terms[-1] += term
            self.terms_cache[self.variables].append(new_terms)
        return self.terms_cache[self.variables][-1]

class PolynomialFactory:
    def __init__(self, data: dict):
        self._data = {
            'degree': 1,
            'variables': 1,
            'terms': [0, 1],
            'ranges': [[0, 1], [0, 1]],
            'mode': 'integer'
        } | data
        self._call = self._call_table[self._data['mode']]

    def integer_mode_call(self) -> Polynomial:
        pass

    def prime_mode_call(self) -> Polynomial:
        pass

    def __call__(self) -> Polynomial:
        """
        Generates a polynomial.
        :return:
        """
        return self._call()

    _call_table: dict[str, Callable[[], Polynomial]] = {
        'integer': integer_mode_call,
        'prime': prime_mode_call,
    }


def main():
    poly = Polynomial(2, 2, [1, 2, 3, 4, 5, 6])
    print(poly)
    print(poly.terms)
    print(poly.evaluate(5, 3))


if __name__ == '__main__':
    main()
