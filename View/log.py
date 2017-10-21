# стандартные бибилеотеки логирования несут сложную инфу .. хоть и организованы легко !
"""
будет класс лог
count - счетик ходов
log_dict.append()
a['1,A']=True


"""
class LOG(object):
    def __init__(self):
        self.log=dict()
        self.count=0

    def set_log(self,str):
        self.log[str]=1
        self.count = self.count+1

    def unique_coordinates(self,str):# если значение нет то вернет TRUE,если оно есть то вернет False
        if(self.log.get(str)is None):

            self.set_log(str)
            return True
        else:

            return False

    def get_log(self,str):
        return self.log.get(str)

    def get_count(self):
        return self.count
