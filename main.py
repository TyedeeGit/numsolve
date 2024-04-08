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
from command import Command, invalid_usage, unknown_command, TYPE_HELP_MSG
from game import Game
from all_games import ALL_GAMES
from typing import Optional

CONTRIBUTORS = (
    'Tyedee',
    'Ammar Abbas'
)




class DefaultGame(Game):
    def __init__(self):
        self.current_game: Optional[Game] = None
        super().__init__(self)

    def stop_game(self):
        verify = input('Are you sure you want to stop? (yes/no) ')
        if verify.lower() == 'yes':
            self.current_game.stop_game()
            self.current_game = None

    def process_command(self, cmd: str):
        match [part for part in cmd.split(' ') if part]:
            case ():
                pass
            case ('help',):
                for command in self._help:
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
            case ('playing',):
                if not self.current_game:
                    print('You are not currently playing a game.')
                else:
                    for game in ALL_GAMES:
                        if game == self.current_game:
                            print(f'Currently playing: {self.current_game._name}')
                            print(self.current_game._about)
                            break
            case ('playing', *_):
                self.handle_invalid_usage('playing')
            case ('games'):
                print('Available games: ')
                for game in ALL_GAMES:
                    print(f'    {game._name}: {game._about}')
            case ('start', game_name):
                if self.current_game:
                    print('Stop the current game before starting a new one.')
                    return True
                for game in ALL_GAMES:
                    if game._name == game_name:
                        self.current_game = game
            case _:
                return False
        return True

    def run(self):
        print('numsolve')
        print(f'MIT License (c) 2024 {", ".join(CONTRIBUTORS)}')
        print(TYPE_HELP_MSG)
        while True:
            cmd = input('> ')
            recognized = False
            if not self.current_game:
                recognized = self.process_command(cmd)
            else:
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
