from typing import Type
from gamelib.game import Game
from .prime_factors.prime_factors import PrimeFactors
from .polynomial_solving.polynomial_solving import PolynomialSolving
from .convergence.convergence import Convergence

ALL_GAMES: tuple[Type[Game], ...] = (
    PrimeFactors,
    PolynomialSolving,
    Convergence
)
