from game.CellOfBoard import CellOfBoard
from game.Board import Board
from game.Ship import Ship


class CoreOfGame(object):
    def __init__(self):
        self.__board = Board
        self.__ships = (Ship(), Ship())     # todo: Заглушка! заменить на гениратор

    def shoot(self, name_cell_of_board):
        target_cell = self.__board.get_cell_of_board(name_cell_of_board)
        if not target_cell:
            pass        # todo: Заглушка! вставить отправку меседжа геймеру
        for ship in self.__ships:
            if not ship.wound():
                target_cell.set_miss_shoot_status()
# todo: Дописать=) 

