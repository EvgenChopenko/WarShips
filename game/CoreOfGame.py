import DataBase.actions_SaveToBD as db
from game.Board import Board
from game.GeneratorOfShip import GeneratorOfShip

MAX_NUMBER_OF_SHOOTS = 50


class CoreOfGame(object):
    def __init__(self, configuration_of_ships):
        self.__num_of_shoots = 0
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
            return False
        is_damage = False
        for ship in self.__ships:
            if ship.make_damage(target_cell):
                is_damage = True
                break
        if not is_damage:
            target_cell.set_miss_shoot_status()
        self.__inc_num_of_shoots()
        return True

    def __inc_num_of_shoots(self):
        self.__num_of_shoots += 1
        if self.__num_of_shoots >= MAX_NUMBER_OF_SHOOTS:
            return True
        return False

    def __get_num_of_shoots(self):
        return self.__num_of_shoots

    def is_exhausted_all_attempts(self):
        if self.__num_of_shoots >= MAX_NUMBER_OF_SHOOTS:
            return True
        return False

    def is_dead_all_ships(self):
        is_alive_ships = False
        for ship in self.__ships:
            is_alive_ships = is_alive_ships or ship.is_alive()
        if is_alive_ships:
            return False
        return True
