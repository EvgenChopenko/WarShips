from game.CellOfBoard import CellOfBoard


class Ship(object):
    def __init__(self):
        self.__decks = list()
        self.__is_alive_ship = None

    def add_deck(self, deck):
        self.__decks.append(deck)

    def make_damage(self, x, y):
        for item in self.__decks:
            if item.is_located(x, y):
                item.set_state(False)
                self.__check_status()
                return True
        return False

    def __check_status(self):
        i = 0
        for item in self.__decks:
            if not item.get_state():
                i += 1
        if i == len(self.__decks):
            self.__is_alive_ship = False

        return False

    def is_alive(self):
        return self.__is_alive_ship


class Deck(object):
    def __init__(self):
        self.__cell = CellOfBoard()
        self.__state = True

    def __set_cell(self, cell):
        if isinstance(cell, CellOfBoard):
            self.__cell = cell
        else:
            raise NotValidValue

    def set_state(self, state):
        if isinstance(state, bool):
            self.__state = state
        else:
            raise NotValidState

    def get_state(self):
        return self.__state

    def is_located(self, cell):
        return self.__cell.equal(cell)


class NotValidState(Exception):
    pass


class NotValidValue(Exception):
    pass
