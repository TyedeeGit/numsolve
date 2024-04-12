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
import fixpath
from math import prod, sqrt, floor
from decimal import Decimal
from typing import Optional
from games.all_games import ALL_GAMES
from gamelib.command import unknown_command, TYPE_HELP_MSG, split_command
from gamelib.game import Game
from gamelib.rational import Rational, parse

CONTRIBUTORS = (
    'Tyedee',
    'Ammar Abbas'
)


class DefaultGame(Game):
    def __init__(self):
        self.current_game: Optional[Game] = None
        super().__init__(self)

    def stop_game(self):
        if not self.current_game:
            print('No game to stop! Did you mean "quit"?')
            return
        verify = input(
            f'Are you sure you want to stop playing: {self.current_game._name} [{self.current_game._id}]? (yes/no) ')
        if verify.lower() == 'yes':
            self.current_game.stop_game()
            print(f'Stopped the current game')
            self.current_game = None

    def add_or_multiply(self, operation: str, *operands: str):
        try:
            if len(operands) < 2:
                raise ValueError('Two or more arguments required!')
            if operation == 'add':
                print(sum(parse(operand) for operand in operands))
            else:
                print(prod(parse(operand) for operand in operands))
        except OverflowError:
            print('Result or input too big!')


    def arithmetic(self, operation: str, arg1: str, arg2: str):
        try:
            match operation:
                case 'sub':
                    print(parse(arg1) - parse(arg2))
                case 'div':
                    print(parse(arg1) / parse(arg2))
                case 'mod':
                    print(int(arg1) % int(arg2))
                case 'exp' | 'pow':
                    print(parse(arg1) ** parse(arg2))
        except OverflowError:
            print('Result or input too big!')
        except ZeroDivisionError:
            print('Division by zero!')

    def sqrt(self, arg: str):
        try:
            r = parse(arg)
            print(Rational(floor(sqrt(r.numerator)), floor(sqrt(r.denominator))))
        except OverflowError:
            print('Input too big!')

    def process_command(self, cmd: str):
        match split_command(cmd):
            case ():
                pass
            case ('help', ):
                for command in self.help:
                    print(command)
            case ('help', command_name):
                found_command = False
                for command in self.help:
                    if command_name == command.name or command_name in command.aliases:
                        print(command)
                        found_command = True
                        break
                if not found_command:
                    print(f'No help message for "{command_name}".')
                    print(TYPE_HELP_MSG)
            case ('help', *_):
                self.handle_invalid_usage('help')
            case ('exit', *_) | ('quit', *_):
                exit()
            case ('playing', *_):
                if not self.current_game:
                    print('You are not currently playing a game. Type "games" for a list of games.')
                else:
                    for game in ALL_GAMES:
                        if game._id == self.current_game._id:
                            print(f'Currently playing: {self.current_game._name} [{self.current_game._id}]')
                            print(self.current_game._about)
                            break
            case ('games', *_):
                print('Available games: ')
                for game in ALL_GAMES:
                    print(f'    {game._name}:\n        About: {game._about}\n        ID: {game._id}')
            case ('start' | 'play', game_id):
                if self.current_game:
                    print('Stop the current game before starting a new one.')
                    return True
                for game in ALL_GAMES:
                    if game._id == game_id:
                        self.current_game = game(self)
                        print(f'Currently playing: {self.current_game._name} [{self.current_game._id}]')
                        print(self.current_game._about)
                        break
                if not self.current_game:
                    print(f'Unknown game id "{game_id}". Type "games" for a list of games and their ids.')
            case ('start' | 'play', *_):
                self.handle_invalid_usage('start')
            case ('stop', *_):
                self.stop_game()
            case (('add' | 'mul') as operation, *operands):
                try:
                    self.add_or_multiply(operation, *operands)
                except ValueError:
                    self.handle_invalid_usage(operation)
            case ((
                  'sub' |
                  'div' |
                  'mod' |
                  'exp' |
                  'pow'
                  ) as operation, arg1, arg2):
                try:
                    self.arithmetic(operation, arg1, arg2)
                except ValueError:
                    self.handle_invalid_usage(operation)
            case ((
                  'sub' |
                  'div' |
                  'mod' |
                  'exp' |
                  'pow'
                  ) as operation, *_):
                self.handle_invalid_usage(operation)
            case ('sqrt', arg):
                try:
                    self.sqrt(arg)
                except ValueError:
                    self.handle_invalid_usage('sqrt')
            case ('sqrt', *_):
                self.handle_invalid_usage('sqrt')
            case (('fraction' | 'frac'), decimal):
                try:
                    integer, fractional = decimal.split('.')
                    fraction = Rational(int(fractional), 10**len(fractional)) + Rational(int(integer), 1)
                    print(fraction)
                except OverflowError:
                    print('Input too big!')
                except ValueError:
                    print('Invalid input!')
            case (('fraction' | 'frac'), *_):
                self.handle_invalid_usage('fraction')
            case (('decimal' | 'deci'), fraction, places):
                try:
                    print(round(parse(fraction), int(places)))
                except OverflowError:
                    print('Input too big!')
                except ValueError:
                    print('Invalid input!')
            case (('decimal' | 'deci'), *_):
                self.handle_invalid_usage('decimal')
            case ('echo', *text):
                print(' '.join(text))
            case _:
                return False
        return True

    def run(self):
        print('Numsolve')
        print(f'MIT License (c) 2024 {", ".join(CONTRIBUTORS)}')
        print(TYPE_HELP_MSG)
        while True:
            recognized = False
            if not self.current_game:
                cmd = input('> ')
                recognized = self.process_command(cmd)
            else:
                cmd = input('>> ')
                recognized = self.current_game.process_command(cmd)
            if not recognized:
                unknown_command()

    @property
    def help(self):
        return self._help if not self.current_game else self.current_game.help


def main():
    default_game = DefaultGame()
    default_game.run()


if __name__ == '__main__':
    main()
