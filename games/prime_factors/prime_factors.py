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

from gamelib.game import Game, default_help
from gamelib.command import Command, split_command
import time
import random

DIFFICULTIES = [
    [(2, 3), (1, 2), (0, 2), (), ()],
    [(0, 4), (1, 4), (0, 3), (0, 1), ()],
    [(0, 4), (1, 4), (1, 4), (0, 2), (0, 1)]
]

PRIMES = [2, 3, 5, 7, 11]

class PrimeFactors(Game):
    _id = 'prime_factors'
    _name = 'Prime Factors'
    _about = 'Figure out prime factors of a number quickly. Type "generate" or "gen" to start. You will be timed.'
    _help = default_help + (
        Command('generate', ('generate',), aliases=('gen',),
                description='Generates a number to factorize. Time will start immediately after using this command.'),
        Command('difficulty', ('difficulty', 'difficulty <level>'), aliases=('diff',),
                description='Sets the difficulty level if provided between 1 and 3. Default is 1.'),
        Command('check', ('check <factors>',), aliases=('c',),
                description='Checks if you have all of the prime factors'),
        Command('answer', ('answer',), aliases=('ans',),
                description='Gives you the answer.')
    )

    def __init__(self, _default_game: Game):
        super().__init__(_default_game)
        self.start_time = 0
        self.number = 1
        self.exponents: list[int, ...] = []
        self.difficulty = 0

    def generate_number(self):
        self.number = 1
        self.exponents = [0] * len(PRIMES)
        for i, prime in enumerate(PRIMES):
            if DIFFICULTIES[self.difficulty][i]:
                self.exponents[i] = random.randint(DIFFICULTIES[self.difficulty][i][0], DIFFICULTIES[self.difficulty][i][1])
                self.number *= prime**self.exponents[i]
        print(f'Your number is: {self.number}')
        self.start_time = time.time()

    def check_factors(self, *factors: str):
        end_time = time.time()
        expected_factors = {f'{prime}^{exponent}' for prime, exponent in zip(PRIMES, self.exponents) if exponent}
        failed = any(factor not in expected_factors for factor in factors) or set(factors) ^ expected_factors
        if failed:
            print('Invalid factors! Try again')
        else:
            print(f'Good job! You factorized {self.number} in {round(end_time-self.start_time, 2)} seconds.')
            self.number = 1

    def give_answer(self):
        end_time = time.time()
        if self.number != 1:
            print(f'The prime factorization of {self.number} = {" * ".join(f"{prime}^{exponent}" for prime, exponent in zip(PRIMES, self.exponents) if exponent)}')
            print(f'You gave up within {end_time-self.start_time:.2f} seconds.')
        self.number = 1

    def process_command(self, cmd: str) -> bool:
        if super().process_command(cmd):
            return True
        match split_command(cmd):
            case ('generate' | 'gen', *_):
                self.generate_number()
            case ('difficulty' | 'diff',):
                print(f'The current difficulty is set to {self.difficulty + 1}')
            case ('difficulty' | 'diff', level):
                try:
                    self.difficulty = int(level) - 1
                    assert self.difficulty in range(0, 3)
                except ValueError:
                    self.handle_invalid_usage('difficulty')
                except AssertionError:
                    print('Please enter an integer between 1 and 3.')
                else:
                    print(f'The current difficulty is now set to {self.difficulty + 1}')
            case ('difficulty' | 'diff', *_):
                self.handle_invalid_usage('difficulty')
            case ('check' | 'c', *factors):
                self.check_factors(*factors)
            case ('answer' | 'ans', *_):
                self.give_answer()
            case _:
                return False
        return True
