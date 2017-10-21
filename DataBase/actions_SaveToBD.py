import os.path as Path

import DataBase.modelBD
#_________________________________________
get_connection= lambda: DataBase.modelBD.connect('WARSHIPS.sqlite')
#______________________________
def creat_shema():
    creation_schema = Path.join(
        Path.dirname(__file__), 'DB.sql')
    with get_connection() as conn:
        DataBase.modelBD.initialize(conn, creation_schema)
################################################
def action_playr_all():
    with get_connection() as conn:
        rows= DataBase.modelBD.playr_all(conn)
    return  rows

def action_player_top_ten():
    with get_connection() as conn:
        rows= DataBase.modelBD.player_top_ten(conn)
    return  rows
#______________________________________________________
def action_add():
    schet=input('schet=' )
    name=input('name= ')

    # if

    #     raise ValueError

    with get_connection() as conn:
        task=DataBase.modelBD.add_new_player(conn, schet, name)

    return task