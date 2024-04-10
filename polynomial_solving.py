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
from typing import Sequence
from game import Game, default_help
from command import Command, split_command
from math import comb
import time
import random
import json


class PolynomialSolving(Game):
    _id = 'polynomial_solving'
    _name = 'Polynomial Solving'
    _about = 'Solve polynomials whose solutions are integers. Use "settings" or "s" to set difficulty. Type "generate" or "gen" to start. You will be timed.'
    _help = default_help + (
        Command('generate', ('generate',), aliases=('gen',),
                description='Generates a polynomial to solve. Time will start immediately after using this command.'),
        Command('settings', ('settings <get|set|help> <setting?>',), aliases=('s', 'difficulty', 'diff'),
                description='Set the difficulty.'),
        Command('check', ('check <args>',), aliases=('c',),
                description='Check your solutions.'),
        Command('answer', ('answer',), aliases=('ans',),
                description='Gives you the answer.')
    )

    def __init__(self, _default_game: Game):
        super().__init__(_default_game)
        with open('polynomial_solving.json') as file:
            self.settings = json.load(file)
        self.current_setting = 'default'

    def process_command(self, cmd: str) -> bool:
        if super().process_command(cmd):
            return True
        match split_command(cmd):
            case ('generate' | 'gen', *_):
                pass
            case (
                ('settings' | 's' | 'difficulty' | 'diff'),
                'get'
            ):
                pass
            case (
                ('settings' | 's' | 'difficulty' | 'diff'),
                'set',
                setting
            ):
                pass
            case (
                ('settings' | 's' | 'difficulty' | 'diff'),
                'help',
                setting
            ):
                pass
            case (
                ('settings' | 's' | 'difficulty' | 'diff'),
                'help'
            ):
                pass
            case (('settings' | 's' | 'difficulty' | 'diff'), 'get' | 'set' | 'help', *_):
                self.handle_invalid_usage('settings')
            case (('settings' | 's' | 'difficulty' | 'diff'), *_):
                self.handle_invalid_usage('settings')
            case ('check' | 'c', *args):
                pass
            case ('answer' | 'ans', *_):
                pass
            case _:
                return False
        return True
