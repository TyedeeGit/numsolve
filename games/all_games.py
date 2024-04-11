from typing import Type
from gamelib.game import Game
from .prime_factors.prime_factors import PrimeFactors
from .polysolve.polysolve import Polysolve
from .convergence.convergence import Convergence

ALL_GAMES: tuple[Type[Game], ...] = (
    PrimeFactors,
    Polysolve,
    Convergence
)
