import sys
class ViewDesk:
<<<<<<< HEAD
=======
    #def __init__(self):


>>>>>>> master
    def show_desk(self, Yabc, X, func):  # 10*10
        first = "%5s|" % ("")
        for i in Yabc:
            first = first + '%5s|' % (str(i))
        s = first + '\n'
        for x in X:
            s = s + '%5d|' % x
            for y in Yabc:
                s = s + "%5s|" % (func.get(str(x) + "," + str(y)))
            s = s + "\n"

        return s
    def action_exit(self):
        sys.exit(0)
    def actions_rules_of_the_game(self):
        """ :return: возврашает текст с правилами
        """
        s = """
Игра просто Космос! 
Перед тобой странная таблица. Включи фантазию  и вспомни как в школе ты играл в морской БОЙ!!  
Морской бой здесь в одни ворота! 
Ты должен вводить координаты в формате {%d,%s}
И за 50 шагов разбить все скрытые корабли .
‘x’- не известное поле 
‘o’- промах 
‘К’ корабль подбит
‘КП ’ – корабль потоплен 
Удачи сухопутный !!\n    
        
        """
<<<<<<< HEAD
        return s
=======
        return s



>>>>>>> master
