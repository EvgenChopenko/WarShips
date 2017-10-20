# todo: Написать метод заполнения координат палуб корабля
class Ship(object):
    def __init__(self, numbers_of_deck):
        self.__decks = [Deck() for i in range(numbers_of_deck)]
        self.__is_alive_ship = True

    def make_damage(self, x, y):
        for item in self.__decks:
            if item.is_destroyed(x, y):
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
        self.__x = -1
        self.__y = -1
        self.__state = True

    def __set_x(self, x):
        if isinstance(x, int):
            self.__x = x
        else:
            raise NotValidValue

    def __set_y(self, y):
        if isinstance(y, int):
            self.__y = y
        else:
            raise NotValidValue

    def set_x_y(self, x, y):
        self.__set_x(x)
        self.__set_y(y)

    def set_state(self, state):
        if isinstance(state, bool):
            self.__state = state
        else:
            raise NotValidState

    def get_state(self):
        return self.__state

    def is_destroyed(self, x, y):
        return self.__x == x and self.__y == y


class NotValidState(Exception):
    pass


class NotValidValue(Exception):
    pass
