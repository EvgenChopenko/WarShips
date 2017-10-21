from game.CellOfBoard import CellOfBoard


class Board(object):
    def __init__(self):
        self.__HORIZONTAL_FRAME = 'ABCDEFGHIJ'
        self.__VERTICAL_FRAME = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.__DICT_OF_DECK = self.__create_dict_of_board()

    def __create_dict_of_board(self):
        vertical_frame = tuple(self.__VERTICAL_FRAME)
        vertical_frame = map(str, vertical_frame)
        key_dict_of_deck = [[i, j] for i in vertical_frame
                            for j in self.__HORIZONTAL_FRAME]
        key_dict_of_deck = tuple(map(','.join, key_dict_of_deck))
        dict_of_deck = dict()
        for item in key_dict_of_deck:
            dict_of_deck[item] = CellOfBoard()
        return dict_of_deck

    def get_horizontal_frame(self):
        return self.__HORIZONTAL_FRAME

    def get_vertical_frame(self):
        return self.__VERTICAL_FRAME

