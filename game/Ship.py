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
                item.wound()
                if not self.__is_alive():
                    self.__kill_ship()
                return True
        return False

    def __is_alive(self):
        i = 0
        for item in self.__decks:
            if not item.get_state():
                i += 1
        if i == len(self.__decks):
            self.__is_alive_ship = False

        return self.__is_alive_ship

    def __kill_ship(self):
        for deck in self.__decks:
            deck.set_ship_is_destroyed_status()


class Deck(object):
    def __init__(self):
        self.__cell = CellOfBoard()
        self.__state = True

    def __set_cell(self, cell):
        if isinstance(cell, CellOfBoard):
            self.__cell = cell
        else:
            raise NotValidValue

    def kill_deck(self):
        self.__cell.set_ship_is_destroyed_status()

    def wound(self):
        self.__state = False
        self.__cell.set_ship_is_damaged_status()

    def get_state(self):
        return self.__state

    def is_located(self, cell):
        return self.__cell.equal(cell)


class NotValidValue(Exception):
    pass
