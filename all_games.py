from typing import Type

from game import Game
from prime_factors import PrimeFactors

ALL_GAMES: tuple[Type[Game], ...] = (
    PrimeFactors,
)
