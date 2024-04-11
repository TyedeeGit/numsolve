from abc import ABC, abstractmethod
from math import comb
from typing import Sequence, Optional


def simplex(n: int, dim: int):
    return comb(n + dim - 1, dim)

def default_vars(length: int):
    return [f'x{i+1}' for i in range(length)]


class Polynomial[CT, VT, RT]:
    terms_cache = {}

    def __init__(self, degree: int, variables: int, coefficients: Sequence[CT], variable_symbols: Optional[Sequence[str]] = None):
        """
        Initializes a Polynomial object.
        """
        self.degree = degree
        self.variables = variables
        if len(coefficients) != len(self.terms):
            raise ValueError(f'Expected {len(self.terms)} coefficients(s), got {len(coefficients)}.')
        self.coefficients = coefficients
        self.variable_symbols = default_vars(variables) if variable_symbols is None else variable_symbols

    def __str__(self):
        output = ''
        not_first_coefficient = False
        for i, (term, coefficient) in enumerate(zip(self.terms, self.coefficients)):
            if coefficient:
                if i and not_first_coefficient:
                    output += ' + ' if coefficient > 0 else ' - '
                output += str(abs(coefficient))
                for var, symbol in zip(term, self.variable_symbols):
                    if var:
                        output += self.variable_symbols[var-1]
                not_first_coefficient = True
        return output

    def evaluate(self, *values: VT) -> RT:
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


class PolynomialFactory[CT, VT, RT](ABC):
    id = ''
    name = ''
    about = ''

    def __init__(self):
        self.settings: dict = {}

    @abstractmethod
    def __call__(self, difficulty: int) -> tuple[Polynomial[CT, VT, RT], tuple[tuple[VT, int], ...], str]:
        """
        Generates a polynomial and a list of zeros.
        :param: difficulty
        :return:
        """
        pass

def main():
    poly = Polynomial(2, 2, [1, 2, 3, 4, 5, 6])
    print(poly)
    print(poly.terms)
    print(poly.evaluate(5, 3))


if __name__ == '__main__':
    main()
