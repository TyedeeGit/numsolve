from typing import Type
from numsolve.gamelib.game import Game
from .prime_factors.prime_factors import PrimeFactors
from .polysolve.polysolve import Polysolve

ALL_GAMES: tuple[Type[Game], ...] = (
    PrimeFactors,
    Polysolve,
)
