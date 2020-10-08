import pymongo
#import dnspython
import sqlite3

password = 'qW1u0T25YK42Ipcm'
dbname = 'test'

def create_mdb_connection(password, dbname):
    client = pymongo.MongoClient(
        'mongodb+srv://Jameshag12:' + password + '@cluster0.vcaf8.mongodb.net/' + dbname + '?retryWrites=true&w=majority'.format(password,dbname)
    )
    return client

def create_sl_connection(extraction_db = "rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(extraction_db)    # local sqlitedb
    return sl_conn

def execute_query(curs, query):
    return curs.execute(query).fetchall()   # Executes query - specifically for SQLite

def character_doc_creation(db, character_table):
    for character in character_table:
        # character = (id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        character_doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8]
            }
        db.insert_one(character_doc)

def show_sl_schema(table):
    schema = "PRAGMA table_info('+ table + ')"

def show_all(db):
    all_docs = list(db.find())
    return all_docs


# SQLite Queiries    sl_conn = create_sl_connection()
get_characters = "SELECT * FROM charactercreator_character;"


if __name__ == "__main__":
    # client = create_connection(password, dbname)
    # db = client.test
    # db.test.insert_one(doc1)
    # db.test.insert_many(all_docs)

    # print(show_all(db))
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(password, dbname)
    db = client.test
    characters = execute_query(sl_curs, get_characters)  # will return a list
    character_doc_creation(db.test, characters)
    print(show_all(db.test))