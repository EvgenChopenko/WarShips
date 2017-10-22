from game.CellOfBoard import CellOfBoard
from game.Board import Board
from game.Ship import Ship
from game.GeneratorOfShip import GeneratorOfShip


class CoreOfGame(object):
    def __init__(self, configuration_of_ships):
        self.__board = Board
        self.__generator_of_ship = GeneratorOfShip(self.__board)

        self.__ships = list()
        for num_of_decks in configuration_of_ships:
            self.__ships.append(self.__generator_of_ship.create_ship(num_of_decks))

    def make_shoot(self, name_cell_of_board):
        target_cell = self.__board.get_cell_of_board(name_cell_of_board)
        if not target_cell:
            pass        # todo: Заглушка! вставить отправку меседжа геймеру
        for ship in self.__ships:
            if not ship.wound():
                target_cell.set_miss_shoot_status()
# todo: Дописать=) 

