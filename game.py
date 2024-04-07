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

from typing import Callable
from abc import ABC, abstractmethod
from command import Command

default_help = (
    Command('help', ('help', 'help cmd'), description='Get information about a command, or list all commands.'),
    Command('add', ('add arg1 arg2',), description='Add two numbers.'),
    Command('sub', ('sub arg1 arg2',), description='Subtract two numbers.'),
    Command('mul', ('mul arg1 arg2',), description='Multiply two numbers.'),
    Command('div', ('div arg1 arg2',), description='Floor divides two numbers.'),
    Command('mod', ('mod arg1 arg2',), description='Modulo operation.'),
    Command('isqrt', ('isqrt arg',), description='Floored square root.'),
    Command('exit', ('exit',), aliases=('quit',), description='Exit the program.'),
    Command('playing', ('playing',), description='Get information about the game your playing')
)

class Game(ABC):
    _help: tuple[Command] = default_help
    def __init__(self, _exit_game: Callable, _default_game: 'Game'):
        self._exit_game = _exit_game
        self._default_game = _default_game

    def exit_game(self):
        self._exit_game()

    def process_command(self, cmd: str) -> bool:
        if self._default_game.process_command(cmd):
            return True
        return False