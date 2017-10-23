class Ship(object):
    def __init__(self):
        self.__decks = list()
        self.__is_alive_ship = None

    def add_deck(self, deck):
        self.__decks.append(deck)
        self.__is_alive_ship = True

    def make_damage(self, cell):
        for item in self.__decks:
            if item.is_located(cell):
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
            deck.kill_deck()

    def is_alive(self):
        return self.__is_alive_ship


class Deck(object):
    def __init__(self, cell):
        self.__cell = cell
        self.__state = True

    def kill_deck(self):
        self.__cell.set_ship_is_destroyed_status()

    def wound(self):
        self.__state = False
        self.__cell.set_ship_is_damaged_status()

    def get_state(self):
        return self.__state

    def is_located(self, cell):
        return self.__cell.equal(cell)
