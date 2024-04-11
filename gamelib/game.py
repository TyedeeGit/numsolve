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
from .command import Command, invalid_usage

default_help = (
    Command('help', ('help', 'help <cmd>'), description='Get information about a command, or list all valid commands. Extra game specific commands may appear.'),
    Command('exit', ('exit',), aliases=('quit',), description='Exit the program.'),
    Command('playing', ('playing',), description='Get information about the game you are currently playing'),
    Command('games', ('games',), description='List all available games.'),
    Command('start', ('start <game_id>',), aliases=('play',), description='Start a game by its id(not name!). Use "games" to get a list of all available games and their ids.'),
    Command('stop', ('stop',), description='Stop the current game.'),
    Command('add', ('add <args>',), description='Add two or more rationals.'),
    Command('sub', ('sub <arg1> <arg2>',), description='Subtract two rationals.'),
    Command('mul', ('mul <args>',), description='Multiply two or more rationals.'),
    Command('div', ('div <arg1> <arg2>',), description='Floor divide two rationals.'),
    Command('mod', ('mod <arg1> <arg2>',), description='Modulo two integers. Second argument is the modulus.'),
    Command('exp', ('exp <arg1> <arg2>',), aliases=('pow',), description='Rational power of two rationals.'),
    Command('sqrt', ('sqrt <arg>',), description='Rational square root of rationals.'),
    Command('echo', ('echo <text>',), description='Echos text.')
)


class Game:
    _id: str = 'game'
    _name: str = 'Base Game'
    _about: str = 'Replace with a description of your game.'
    _help: tuple[Command] = default_help

    def __init__(self, _default_game: 'Game'):
        self._default_game = _default_game

    def __eq__(self, other: 'Game'):
        return self._id == other._id and self._about == other._about

    def stop_game(self):
        pass

    def process_command(self, cmd: str) -> bool:
        return self._default_game.process_command(cmd)

    def handle_invalid_usage(self, cmd_name: str):
        print(invalid_usage(self.get_command_by_name(cmd_name)))

    def get_command_by_name(self, cmd_name: str) -> Command:
        for cmd in self.help:
            if cmd.name == cmd_name:
                return cmd

    @property
    def help(self):
        return self._help
