"""
Copyright (c) 2024 Tyedee

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
import json
from time import time
from typing import Optional
from gamelib.command import Command, split_command
from gamelib.game import Game, default_help
from gamelib.polynomial import Polynomial, PolynomialFactory
from gamelib.polynomial_factories import find_factory


class PolynomialSolving(Game):
    _id = 'polynomial_solving'
    _name = 'Polynomial Solving'
    _about = 'Solve polynomials whose solutions are integers. Use "settings" or "s" to set difficulty. Type "generate" or "gen" to start. You will be timed.'
    _help = default_help + (
        Command('generate', ('generate',), aliases=('gen',),
                description='Generates a polynomial to solve. Time will start immediately after using this command.'),
        Command('mode', ('mode <get|set|help> <mode?>',), aliases=('m',),
                description='Set or get the polynomial generation mode.'),
        Command('difficulty', ('difficulty', 'difficulty <level>'), aliases=('diff',),
                description='Set or get the polynomial generation difficulty'),
        Command('check', ('check <args>',), aliases=('c',),
                description='Check your solutions.'),
        Command('answer', ('answer',), aliases=('ans',),
                description='Gives you the answer.')
    )

    def __init__(self, _default_game: Game):
        super().__init__(_default_game)
        self.current_mode = 'default'
        self.current_difficulty = "1"
        self.current_polynomial: Optional[Polynomial] = None
        self.current_factory: Optional[PolynomialFactory] = None
        self.start_time = 0
        self.solutions: tuple[str, ...] = ()
        self.update_factory()

    def update_settings(self):
        if self.current_factory:
            with open('games/polynomial_solving/polynomial_solving.json') as file:
                self.current_factory.settings = json.load(file)[self.current_mode]

    def update_factory(self):
        self.current_factory = find_factory(self.current_mode)()
        self.update_settings()

    def check_answer(self, *answers: str):
        end_time = time()
        if answers == self.solutions:
            print(f'You solved the polynomial in {end_time - self.start_time:.2f} seconds!')
            self.update_factory()
            self.current_polynomial = None
        else:
            print('Incorrect answer. Try again.')

    def process_command(self, cmd: str) -> bool:
        if super().process_command(cmd):
            return True
        match split_command(cmd):
            case ('generate' | 'gen', *_):
                self.current_polynomial, self.solutions, problem = self.current_factory(self.current_difficulty)
                print(f'Problem: {problem}')
                self.start_time = time()
            case (('mode' | 'm'), 'get'):
                print()
            case (('mode' | 'm'), 'get' | 'set' | 'help', *_):
                self.handle_invalid_usage('mode')
            case (('difficulty' | 'diff'), *_):
                self.handle_invalid_usage('settings')
            case ('check' | 'c', *args):
                self.check_answer(*args)
            case ('answer' | 'ans', *_):
                end_time = time()
                print('Solution:')
                for symbol, solution in zip(self.current_polynomial.variable_symbols, self.solutions):
                    print(f'{symbol} = {solution}')
                print(f'You gave up in {end_time - self.start_time:.2f} seconds!')
                self.current_polynomial = None
            case _:
                return False
        return True
