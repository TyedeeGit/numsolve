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

from numsolve.gamelib.game import Game, default_help
from numsolve.gamelib.command import Command, split_command
from numsolve.gamelib.rational import Rational, parse
from numsolve.gamelib.series import GeometricSeries
from random import randint


class Convergence(Game):
    _id = 'convergence'
    _name = 'Convergence'
    _about = 'Practice convergence tests on infinite series.'
    _help = default_help + (
        Command('formula', ('formula',),
                description='Generates the formula for finding the sum of an infinite series.'),
        Command('generate', ('generate', 'generate <starting_value> <ratio>',), aliases=('gen',),
                description='Generates an infinite series.')
    )

    def __init__(self, _default_game: Game):
        super().__init__(_default_game)
        self.current_series = None

    def generate(self, starting_value: str, ratio: str):
        self.current_series = GeometricSeries(parse(starting_value), parse(ratio))

    def generate_random(self):
        self.current_series = GeometricSeries(Rational(randint(1, 10), randint(1, 10)),
                                              Rational(randint(1, 10), randint(1, 10)))

    def get_formula(self):
        if self.current_series is None:
            print('No series to generate formula for. Type "generate" or "gen" to generate a series.')
            return
        print(f'{self.current_series.starting_value} / (1 - {self.current_series.ratio})')

    def process_command(self, cmd: str) -> bool:
        if super().process_command(cmd):
            return True

        match split_command(cmd):
            case ('formula', *_):
                self.get_formula()
            case _:
                return False
        return True
