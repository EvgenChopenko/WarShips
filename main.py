def main():
    pass

import View.menu
import View.actions_desk
import View.log
import DataBase.actions_SaveToBD as DB
#todo :пример
dict={'1,A':'К','2,A':'none'}

menu=View.menu.Menu()
show = View.actions_desk.ViewDesk()
menu.create_menu(id='!M',func= menu.show_menu,name='меню')
menu.create_menu(id='!D',func= View.actions_desk.ViewDesk().show_desk,name='Вывести игровое поле')
menu.create_menu(id='!Q',func=View.actions_desk.ViewDesk().action_exit,name='Выход из игры ')
menu.create_menu(id='!1',func='',name='Вывести список играков')
menu.create_menu(id='!2',func='',name='Начать заново')
menu.create_menu(id='!3',func=View.actions_desk.ViewDesk().action_exit,name='Правила иргы')

print(menu.show_menu())




print(menu.call_actions(id='!D')('ABCDEFGHIJ',[1,2,3,4,5,6,7,8,9,10],dict))
#print(show.show_desk('ABCDEFGHIJ',[1,2,3,4,5,6,7,8,9,10],dict))


# DB.creat_shema()
# DB.action_add()
# print(DB.action_playr_all())
# print(DB.action_player_top_ten())
log = View.log.LOG()
print(log.unique_coordinates('1,A'))
print(log.unique_coordinates('1,A'))
print(log.unique_coordinates('1,B'))
print(log.unique_coordinates('1,A'))
print(log.get_count())