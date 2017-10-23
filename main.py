def main():
    pass

import View.view
from  game.CoreOfGame  import CoreOfGame
# DB.creat_shema()
# DB.action_add()
# print(DB.action_playr_all())
# print(DB.action_player_top_ten())

configuration_of_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
games = CoreOfGame(configuration_of_ships)
v=View.view.view(games.get_board())
v.initialization()

print(v.showboard())
# print(v._input())
while True:
    s = v._input(games.make_shoot, games.is_dead_all_ships)
    if s is True:
        break

    print(v.showboard())

print("Winner")
