# todo: Menu - хранит class c с пунктами мюню, и ссылки на actions,
import json
"""
это класс нужен для создания меню,
хранаения функций пунктов меню,
возврашет список ключ:загалово меню(вопрос),
возврашает функцию по ключу 
"""
# coding: utf8
from collections import namedtuple, OrderedDict, Iterable


class Menu(object):
    def __init__(self):
        self.Action = namedtuple('Action', ['func', 'name'])# хранит связку заголово меню (вопрос) и функцию
        self.actions = OrderedDict()# хранит id: и связку
#_______________________________________________________________________________________________________________

    def create_menu(self,id,func,name):
        if(self.actions.get(id) is None):# зашита от повторений
            self.actions[id]=self.Action(func=func,name=name)# создание меню
        else:
            raise KeyError ("id повторилось! при создании Меню")
#_________________________________________________________________________________________________________________


    def show_menu(self):
        """Показать меню"""
        menu = []# формирться кортедж который состоит id (команда вызова ): загаловок

        for cmd, action in self.actions.items():
            menu.append('{}. {}'.format(cmd, action.name))

        return ('\n'.join(menu))
#_____________________________________________________________________________________________________________________
    def call_actions(self,id):# возврашает сылку выполняемой функции  по команде ввода.
        try:
            s=self.actions[id]
            return s.func
        except:
            return None
#_____________________________________________________________________________________________________________________
    def call_name(self, id):  # возврашает имя заголовка для меню .
        if (self.actions.get(id) is None):  # зашита от промаха
            s = self.actions[id]
        else:
            raise KeyError ("id не найден")
        return s.name
#_____________________________________________________________________________________________________________________
    def watch_command_run(self,id):# обробатывет запрос  (id) -> и возврашаеь вызов
       # id=input("Введите ваш следуюший ход :")
        try:
            return self.call_name(id)
        except :
            return None

#______________________________________________________________________________________________________________________