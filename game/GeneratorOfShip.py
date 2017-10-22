import random
from game.CellOfBoard import CellOfBoard
from game.Board import Board
import game.Ship as ship_pack


class GeneratorOfShip(object):
    def __init__(self, board):
        self.__board = board
        self.__list_of_free_cells = list(self.__board.get_names_of_cells())
        self.__HORIZONTAL_ALPHABET = list(self.__board.get_horizontal_frame())
        self.__VERTICAL_ALPHABET = list(map(str, self.__board.get_vertical_frame()))
        self.__ALPHABET_FOR_GENERATING_CELL_NAMES = self.__VERTICAL_ALPHABET + self.__HORIZONTAL_ALPHABET

    def create_ship(self, number_of_decks):
        inc_component, const_component = self.__generate_allowed_position_of_ship(number_of_decks)
        names_of_position = self.__generate_names_of_position(inc_component, const_component)
        names_of_forbidden_position = self.__generate_names_forbidden_position(inc_component, const_component)
        ship = ship_pack.Ship()
        for item in names_of_position:
            cell = self.__board.get_cell_of_board(item)
            deck = ship_pack.Deck(cell)
            ship.add_deck(deck)

        self.__forbid_positions(names_of_position)
        self.__forbid_positions(names_of_forbidden_position)
        return ship

    def __forbid_positions(self, positions):
        for item in positions:
            if self.__is_free_cell(item):
                self.__list_of_free_cells.remove(item)

    def __generate_allowed_position_of_ship(self, number_of_decks):
        inc_component, const_component = self.__generate_position_of_ship(number_of_decks)
        names_of_position = self.__generate_names_of_position(inc_component, const_component)
        while not self.__is_allowed_position_of_ship(names_of_position):
            inc_component, const_component = self.__generate_position_of_ship(number_of_decks)
            names_of_position = self.__generate_names_of_position(inc_component, const_component)
        return inc_component, const_component

    def __generate_position_of_ship(self, number_of_decks):
        positions_of_ship = None
        while not positions_of_ship:
            index_of_inc_component = random.randint(0, len(self.__ALPHABET_FOR_GENERATING_CELL_NAMES) - 1)
            inc_component = list()
            inc_component.append(self.__ALPHABET_FOR_GENERATING_CELL_NAMES[index_of_inc_component])
            if inc_component[0].isdigit():
                positions_of_ship = self.__generate_position_of_decks(number_of_decks, inc_component)
            else:
                positions_of_ship = self.__generate_position_of_decks(number_of_decks, inc_component)

        return positions_of_ship

    def __generate_position_of_decks(self, number_of_decks, inc_component):
        inc_alphabet, const_alphabet, index_of_inc_component = self.__define_alphabets_and_idx(inc_component)

        for i in range(1, number_of_decks):
            index_of_inc_component += 1
            if index_of_inc_component < len(inc_alphabet):
                inc_component.append(inc_alphabet[index_of_inc_component])
            else:
                return None
        const_component = const_alphabet[random.randint(0, len(const_alphabet) - 1)]

        return inc_component, const_component

    def __define_alphabets_and_idx(self, inc_component):
        if inc_component[0].isdigit():
            inc_alphabet = self.__VERTICAL_ALPHABET
            const_alphabet = self.__HORIZONTAL_ALPHABET
        else:
            inc_alphabet = self.__HORIZONTAL_ALPHABET
            const_alphabet = self.__VERTICAL_ALPHABET
        index_of_inc_component = inc_alphabet.index(inc_component[0])
        return inc_alphabet, const_alphabet, index_of_inc_component

    def __generate_names_of_position(self, inc_component, const_component):
        positions_of_decks = list()
        if inc_component[0].isdigit():
            for item in inc_component:
                positions_of_decks.append(','.join((item, const_component)))
        else:
            for item in inc_component:
                positions_of_decks.append(','.join((const_component, item)))
        return positions_of_decks

    def __generate_names_forbidden_position(self, inc_component, const_component):
        temp = list()
        temp.append(self.__generate_names_forbidden_front_position(inc_component, const_component))
        temp.append(self.__generate_names_forbidden_back_position(inc_component, const_component))
        temp.append(self.__generate_names_forbidden_left_position(inc_component, const_component))
        temp.append(self.__generate_names_forbidden_right_position(inc_component, const_component))
        forbidden_position = list()
        for item in temp:
            if item:
                forbidden_position += item
        return forbidden_position

    def __generate_names_forbidden_front_position(self, inc_component, const_component):
        inc_alphabet, const_alphabet, index_of_inc_component = self.__define_alphabets_and_idx(inc_component)
        index_of_const_component = const_alphabet.index(const_component)
        forbidden_inc_component = list()
        index_of_forbidden_const_component = index_of_inc_component - 1
        if index_of_forbidden_const_component < 0:
            return None
        else:
            forbidden_const_component = inc_alphabet[index_of_forbidden_const_component]

        if index_of_const_component - 1 >= 0:
            forbidden_inc_component.append(const_alphabet[index_of_const_component - 1])

        forbidden_inc_component.append(const_alphabet[index_of_const_component])

        if index_of_const_component + 1 < len(const_alphabet):
            forbidden_inc_component.append(const_alphabet[index_of_const_component + 1])

        return self.__generate_names_of_position(forbidden_inc_component, forbidden_const_component)

    def __generate_names_forbidden_back_position(self, inc_component, const_component):
        inc_alphabet, const_alphabet, index_of_inc_component = self.__define_alphabets_and_idx(inc_component)
        index_of_const_component = const_alphabet.index(const_component)
        forbidden_inc_component = list()
        index_of_forbidden_const_component = index_of_inc_component + len(inc_component)
        if index_of_forbidden_const_component < len(inc_alphabet):
            forbidden_const_component = inc_alphabet[index_of_forbidden_const_component]
        else:
            return None

        if index_of_const_component - 1 >= 0:
            forbidden_inc_component.append(const_alphabet[index_of_const_component - 1])

        forbidden_inc_component.append(const_alphabet[index_of_const_component])

        if index_of_const_component + 1 < len(const_alphabet):
            forbidden_inc_component.append(const_alphabet[index_of_const_component + 1])

        return self.__generate_names_of_position(forbidden_inc_component, forbidden_const_component)

    def __generate_names_forbidden_left_position(self, inc_component, const_component):
        inc_alphabet, const_alphabet, index_of_inc_component = self.__define_alphabets_and_idx(inc_component)
        index_of_const_component = const_alphabet.index(const_component)
        index_of_forbidden_const_component = index_of_const_component - 1
        if index_of_forbidden_const_component < 0:
            return None
        else:
            forbidden_const_component = const_alphabet[index_of_forbidden_const_component]

        forbidden_inc_component = inc_component

        return self.__generate_names_of_position(forbidden_inc_component, forbidden_const_component)

    def __generate_names_forbidden_right_position(self, inc_component, const_component):
        inc_alphabet, const_alphabet, index_of_inc_component = self.__define_alphabets_and_idx(inc_component)
        index_of_const_component = const_alphabet.index(const_component)
        index_of_forbidden_const_component = index_of_const_component + 1
        if index_of_forbidden_const_component < len(const_alphabet):
            forbidden_const_component = const_alphabet[index_of_forbidden_const_component]
        else:
            return None

        forbidden_inc_component = inc_component

        return self.__generate_names_of_position(forbidden_inc_component, forbidden_const_component)

    def __is_allowed_position_of_ship(self, position):
        for item in position:
            if not self.__is_free_cell(item):
                return False
        return True

    def __is_free_cell(self, cell_name):
        if not (cell_name in self.__list_of_free_cells):
            return False
        return True
