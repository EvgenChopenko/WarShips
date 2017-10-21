class CellOfBoard(object):
    def __init__(self):
        self.__STATUSES_OF_CELL = {'DEFAULT_VALUE': 'о',
                                   'MISS_SHOOT': 'х',
                                   'SHIP_IS_DAMAGED': 'К',
                                   'SHIP_IS_DESTROYED': 'КП'}

        self.__status = self.__STATUSES_OF_CELL.get('DEFAULT_VALUE')

    def equal(self, cell):
        return self == cell

    def visible(self):
        return self.__status

