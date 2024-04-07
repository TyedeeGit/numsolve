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

from dataclasses import dataclass
from sys import stderr

TYPE_HELP_MSG = 'Type "help" for a list of commands.'

def unknown_command():
    print(f'Unknown command.\n{TYPE_HELP_MSG}')

HELP_FORMAT = '''{name}: {description}
    Aliases:
{aliases}
    Usages:
{usages}
'''

HELP_FORMAT_NO_ALIASES = '''{name}: {description}
    Usages:
{usages}
'''

@dataclass
class Command:
    name: str
    usages: tuple[str, ...]
    aliases: tuple[str, ...] = ()
    description: str = ""

    def __str__(self):
        aliases = '\n'.join(f'        {alias}' for alias in self.aliases)
        usages = '\n'.join(f'        {usage}' for usage in self.usages)
        if not aliases:
            return HELP_FORMAT_NO_ALIASES.format(
                name=self.name,
                description=self.description,
                usages=usages
            )
        return HELP_FORMAT.format(
            name=self.name,
            description=self.description,
            aliases=aliases,
            usages=usages
        )

def invalid_usage(cmd: Command) -> str:
    return f'Valid usages:{"".join(f'\n    {usage}' for usage in cmd.usages)}'
