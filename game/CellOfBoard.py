class CellOfBoard(object):
    def __init__(self):
        self.__STATUSES_OF_CELL = {'DEFAULT_VALUE': 'о',
                                   'MISS_SHOOT': 'х',
                                   'SHIP_IS_DAMAGED': 'К',
                                   'SHIP_IS_DESTROYED': 'КП'}

        self.__status = self.__STATUSES_OF_CELL.get('DEFAULT_VALUE')

    def equal(self, cell):
        return self == cell

    def set_default_status(self):
        self.__status = self.__STATUSES_OF_CELL.get('DEFAULT_VALUE')

    def set_miss_shoot_status(self):
        self.__status = self.__STATUSES_OF_CELL.get('MISS_SHOOT')

    def set_ship_is_damaged_status(self):
        self.__status = self.__STATUSES_OF_CELL.get('SHIP_IS_DAMAGED')

    def set_ship_is_destroyed_status(self):
        self.__status = self.__STATUSES_OF_CELL.get('SHIP_IS_DESTROYED')

    def visible(self):
        return self.__status

