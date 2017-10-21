import sqlite3
#_____________________________________________________________________________________________________
SQL_SELECT_ALL = """ SELECT ID, DataCreate, Schet, NamePlayer FROM WARSHIPS"""

SQL_SELECT_TOP_TEN="""SELECT DataCreate, Schet, NamePlayer FROM WARSHIPS

ORDER BY Schet DESC LIMIT 10; """


#----------------------------------------------------------------------------------------------------------------
SQL_INSERT_NEW = """INSERT INTO WARSHIPS (Schet, NamePlayer) VALUES (?,?)"""
#----------------------------------------------------------------------------------------------------------------------
SQL_UPDATE_Schet="""UPDATE WARSHIPS set Schet = ? WHERE id = ?"""

SQL_UPDATE_NamePlayer="""UPDATE WARSHIPS set NamePlayer = ? WHERE id = ?"""

SQL_UPDATE_DataCreate="""UPDATE WARSHIPS set DataCreate = ? WHERE id = ?"""

#---------------------------------------------------------------------
#________________________________________________________
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#_______________________________________________________________________________________________________________
def connect(db_name=None):
    if db_name is None:
        db_name=':memory:'
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn

def initialize(conn,creation_shema):
    with conn,open(creation_shema) as f:
        conn.executescript(f.read())
#_________________________________________________________________________________________________________________
def add_new_player(conn,Schet,NamePlayer):
    with conn:
        cursor = conn.execute(SQL_INSERT_NEW,(Schet,NamePlayer))
#__________________________________________________________________________________________________________________
def playr_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
    return cursor.fetchall()

def player_top_ten(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_TOP_TEN)
    return cursor.fetchall()

#____________________________________________________________________________________________________________________
def update(conn):
    def update_Schet(values,id):
        with conn:
            cursor = conn.execute(SQL_UPDATE_Schet,(values,id))
    def update_NamePlayer(values,id):
        with conn:
            cursor = conn.execute(SQL_UPDATE_NamePlayer,(values, id))
    def update_DataCreate(values,id):
        with conn:
            cursor = conn.execute(SQL_UPDATE_DataCreate,(values, id))

    return update_Schet, update_NamePlayer,update_DataCreate



