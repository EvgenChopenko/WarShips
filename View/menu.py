# todo: Menu - хранит class c с пунктами мюню, и ссылки на actions,
import json

# coding: utf8
from collections import namedtuple, OrderedDict, Iterable


class Menu(object):
    def __init__(self):
        self.Action = namedtuple('Action', ['func', 'name'])
        self.actions = OrderedDict()


    def create_menu(self,id,func,name):
        self.actions[id]=self.Action(func=func,name=name)


    # def write(self):
    #     with open('menu.json','w') as f:
    #         json.dump(f,self.actions,indent=4)
    # можно писать в json но не знаю зачем.

    def show_menu(self):
        """Показать меню"""
        menu = []

        for cmd, action in self.actions.items():
            menu.append('{}. {}'.format(cmd, action.name))

        return ('\n'.join(menu))

    def call_actions(self,id):# возврашает сылку выполняемой функции  по команде ввода.
        try:
            s=self.actions[id]
            return s.func
        except:
            return None

    def call_name(self, id):  # возврашает имя заголовка для меню .


        s = self.actions[id]



        return s.name

    def watch_command_run(self,id):# обробатывет запрос  (id) -> и возврашаеь вызов
       # id=input("Введите ваш следуюший ход :")
        try:
            return self.call_name(id)
        except :
            return None

