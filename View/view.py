import View.menu
import View.actions_desk
import View.log
import re
dict={'1,A':'К','2,A':'none'}# временный файл!
class view:
    def __init__(self):# объекты протипов класса создаються в конструкторе
        self.menu = View.menu.Menu()
        self.actions = View.actions_desk.ViewDesk()
        self.log = View.log.LOG()

#______________________________________________________________________________________________________________________
    def initialization(self):# генерация меню !
        self.menu.create_menu(id='!M', func=self.menu.show_menu, name='меню')
        self.menu.create_menu(id='!D', func=self.actions.show_desk, name='Вывести игровое поле')
        self.menu.create_menu(id='!Q', func=self.actions.action_exit, name='Выход из игры ')
        self.menu.create_menu(id='!1', func='', name='Вывести список играков')
        self.menu.create_menu(id='!2', func='', name='Начать заново')
        self.menu.create_menu(id='!3', func=self.actions.actions_rules_of_the_game, name='Правила иргы')
        #self.menu.create_menu(id='!D', func=self.actions.show_desk, name='Вывести игровое поле')

#______________________________________________________________________________________________________________________

    def valid(self,text):# Валидность проврка даных приемлимый результат [1,A] - A -английская
        text = text.upper()# все значения в верхний регистр

        parser = re.search('\d,\w', text)# в полученном тексте нахдим конструкцию число,символ-число
        try:
            text = parser.group()  # переписывет текст если найденна консрукция
        except:
            return None # если констуркция не найдена то вернет None

        if (text[-1].isdigit()):# проверка на то что символ после запятой число и возрошает none
            return None
        if (text[-1].isalpha()):# праверка что символ это буква
            a = str.maketrans('', '', 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ') # Удалаение русской раскладки

            if (text != text.translate(a)):# сравнивает исходный текст с текстом в котором удалили русскую раскладку
                return None# если они не равны то вернут none

                # text=None

        return text# найденный адресс
#______________________________________________________________________________________________________________________
    def _input(self):
        command = input("Ваш слеуюший ход: ")
        func = self.menu.call_actions(command)
        if (func is None):
            text = self.valid(command)
            if (text is not None):
                if self.log.unique_coordinates(command):
                   # запрос к боард if boar_true  тогда да ели не верни повтори ввод

                   return (self.menu.call_actions(id='!D')(Yabc='ABCDEFGHIJ',X=[1,2,3,4,5,6,7,8,9,10],func=dict))# заглушка
                else:
                    return ('Повтори ввод! ')


        else:
            return func()
#_______________________________________________________________________________________________________________________
#print(menu.show_menu())

#print(menu.call_actions(id='!D')('ABCDEFGHIJ',[1,2,3,4,5,6,7,8,9,10],dict))



# print(log.unique_coordinates('1,A'))
# print(log.unique_coordinates('1,A'))
# print(log.unique_coordinates('1,B'))
# print(log.unique_coordinates('1,A'))
# print(log.get_count())

# #todo :пример
# dict={'1,A':'К','2,A':'none'}