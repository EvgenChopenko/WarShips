from game.CellOfBoard import CellOfBoard
from game.Board import Board
from game.Ship import Ship
from game.GeneratorOfShip import GeneratorOfShip
import DataBase.actions_SaveToBD as db


class CoreOfGame(object):
    def __init__(self, configuration_of_ships):
        self.__board = Board()
        self.__generator_of_ship = GeneratorOfShip(self.__board)

        self.__ships = list()
        for num_of_decks in configuration_of_ships:
            self.__ships.append(self.__generator_of_ship.create_ship(num_of_decks))
        db.creat_shema()

    def get_board(self):
        return self.__board

    def make_shoot(self, name_cell_of_board):
        target_cell = self.__board.get_cell_of_board(name_cell_of_board)
        if not target_cell:
            return None
        is_alive_ship = False
        for ship in self.__ships:
            if not ship.make_damage(target_cell):
                target_cell.set_miss_shoot_status()
                is_alive_ship = is_alive_ship or ship.is_alive()
        if is_alive_ship:
            return False
        return True
