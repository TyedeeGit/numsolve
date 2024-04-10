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

from game import Game, default_help
from command import Command, split_command

class ExampleGame(Game):
    _id = 'example'
    _about = 'Example game to help contributors make their own.'
    _help = default_help + (
        Command('example', ('example <arg1> <arg2>',), aliases=('alias1', 'alias2'), description='Example command.'),
    )

    def __init__(self, _default_game: Game):
        super().__init__(_default_game)
        self.example_var = 2

    def example_command(self, arg1: str, arg2: str):
        print(f"You used 'example {arg1} {arg2}'!")

    def process_command(self, cmd: str) -> bool:
        if super().process_command(cmd):
            return True

        match split_command(cmd):
            case ('example', arg1, arg2):
                self.example_command(arg1, arg2)
            case ('example', *_):
                self.handle_invalid_usage('example')
            case _:
                return False
        return True