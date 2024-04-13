from typing import Type, Optional
from .polynomial import PolynomialFactory, Polynomial
from numsolve.gamelib.rational import Rational
from numsolve.gamelib.primes import get_primes_in_range
from random import randint


class DefaultPolynomialFactory[CT: int, VT: int, RT: int](PolynomialFactory):
    id = 'default'
    name = 'Simon\'s Favorite Polynomials'
    about = 'Generates a polynomial Apq + Bp + Cq - D = 0, where p and q are primes.'

    def __call__(self, difficulty: int) -> tuple[Polynomial[CT, VT, RT], tuple[VT, ...], str, str]:
        primes = [prime for prime in get_primes_in_range(2, self.settings[difficulty]['prime_range'][1]+1)]

        p, q = (primes[randint(primes.index(self.settings[difficulty]['prime_range'][0]), len(primes)-1)],
                primes[randint(primes.index(self.settings[difficulty]['prime_range'][0]), len(primes)-1)])

        a, b, c = (randint(*self.settings[difficulty]['a_range']),
                   randint(*self.settings[difficulty]['b_range']),
                   randint(*self.settings[difficulty]['c_range']))

        d = a*p*q + b*p + c*q
        polynomial = Polynomial(2, 2, [0, a, 0, b, c, -d], variable_symbols=['q', 'p'])
        return polynomial, (str(q), str(p)), f'{polynomial} = 0, where q and p are primes. Solutions must be given in reverse order.', f'q = {q}\np = {p}'

    def check(self, polynomial: Polynomial[CT, VT, RT], solutions: tuple[VT, ...], answers: tuple[str, ...]) -> bool:
        parsed_answers: list[Rational, ...] = [int(answer) for answer in answers]
        return not polynomial.evaluate(*parsed_answers)

ALL_POLYNOMIAL_FACTORIES: tuple[Type[PolynomialFactory], ...] = (
    DefaultPolynomialFactory,
)

def find_factory(_id: str) -> Optional[Type[PolynomialFactory]]:
    for factory in ALL_POLYNOMIAL_FACTORIES:
        if factory.id == _id:
            return factory