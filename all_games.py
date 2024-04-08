from typing import Type
from game import Game
from prime_factors import PrimeFactors
from polynomial_solving import PolynomialSolving

ALL_GAMES: tuple[Type[Game], ...] = (
    PrimeFactors,
    PolynomialSolving
)
