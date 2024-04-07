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
from command import Command, invalid_usage

default_help = (
    Command('help', ('help', 'help cmd'), description='Get information about a command, or list all commands.'),
    Command('exit', ('exit',), aliases=('quit',), description='Exit the program.'),
    Command('playing', ('playing',), description='Get information about the game you are currently playing'),
    Command('games', ('games',), description='List all available games.'),
    Command('start', ('start game_name',), description='Start a game. Use "games" to get a list of all available games.'),
    Command('stop', ('stop',), description='Stop the current game.'),
    Command('add', ('add arg1 arg2',), description='Add two numbers.'),
    Command('sub', ('sub arg1 arg2',), description='Subtract two numbers.'),
    Command('mul', ('mul arg1 arg2',), description='Multiply two numbers.'),
    Command('div', ('div arg1 arg2',), description='Floor divides two numbers.'),
    Command('mod', ('mod arg1 arg2',), description='Modulo operation.'),
    Command('isqrt', ('isqrt arg',), description='Floored square root.'),
)


class Game(ABC):
    _name: str = 'game'
    _about: str = 'Replace with a description of your game.'
    _help: tuple[Command] = default_help

    def __init__(self, _default_game: 'Game'):
        self._default_game = _default_game

    def __eq__(self, other: 'Game'):
        return self._name == other._name and self._about == other._about

    def stop_game(self):
        pass

    def process_command(self, cmd: str) -> bool:
        if self._default_game.process_command(cmd):
            return True
        return False

    def handle_invalid_usage(self, cmd_name: str):
        print(invalid_usage(self.get_command_by_name(cmd_name)))

    def get_command_by_name(self, cmd_name: str) -> Command:
        for cmd in self.help:
            if cmd.name == cmd_name:
                return cmd

    @property
    def help(self):
        return self._help