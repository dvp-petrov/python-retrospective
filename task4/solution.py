class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard(dict):
    def __init__(self):
        self.winner = ''
        dict.__init__(self)
        self.update({
            'A1': ' ',
            'A2': ' ',
            'A3': ' ',
            'B1': ' ',
            'B2': ' ',
            'B3': ' ',
            'C1': ' ',
            'C2': ' ',
            'C3': ' ', })

    def __setitem__(self, key, item):
        x_count = len([x for x in self.values() if x == 'X'])
        o_count = len([o for o in self.values() if o == 'O'])
        try:
            if key not in self.keys():
                raise InvalidKey
            if self[key] == 'O' or self[key] == 'X':
                raise InvalidMove
            if item not in ['X', 'O']:
                raise InvalidValue
            if (x_count > o_count and item == 'X' or
                    x_count < o_count and item == 'O'):
                raise NotYourTurn
            super(TicTacToeBoard, self).__setitem__(key, item)
        except InvalidKey:
            raise InvalidKey
        except InvalidMove:
            raise InvalidMove
        except InvalidValue:
            raise InvalidValue
        except NotYourTurn:
            raise NotYourTurn
        else:
            first_winner = self.game_status()
            if 'win' in first_winner and not self.winner:
                self.winner = first_winner

    def __str__(self):
        return '\n  -------------\n' +\
            '3 | ' + self['A3'] + ' | ' + self['B3'] + ' | ' \
            + self['C3'] + ' |\n' +\
            '  -------------\n' +\
            '2 | ' + self['A2'] + ' | ' + self['B2'] + ' | ' \
            + self['C2'] + ' |\n' +\
            '  -------------\n' +\
            '1 | ' + self['A1'] + ' | ' + self['B1'] + ' | ' \
            + self['C1'] + ' |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'

    def game_status(self):
        if self.winner:
            return self.winner
        winner_list = [[self['A1'], self['A2'], self['A3']],
                       [self['B1'], self['B2'], self['B3']],
                       [self['C1'], self['C2'], self['C3']],
                       [self['A1'], self['B1'], self['C1']],
                       [self['A2'], self['B2'], self['C2']],
                       [self['A3'], self['B3'], self['C3']],
                       [self['A1'], self['B2'], self['C3']],
                       [self['A3'], self['B2'], self['C1']]]
        X_or_O = ''
        for element in winner_list:
            if element == ['X', 'X', 'X']:
                X_or_O = 'X'
            elif element == ['O', 'O', 'O']:
                X_or_O = 'O'
        if X_or_O:
            self.winner = X_or_O + ' wins!'
            return (X_or_O + ' wins!')
        else:
            for value in self.values():
                if value == ' ':
                    return 'Game in progress.'
            return 'Draw!'
