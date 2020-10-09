import sqlite3


def connect_to_db(db_name = 'demo_data.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

create_statement = 'CREATE TABLE demo (s TEXT, x INT, y INT);'

insert_statement = """
    INSERT INTO demo (s, x, y)
    VALUES ('g', 3, 9),    
    ('v', 5, 7),
    ('f', 8, 7);

"""

get_rows = """
    SELECT *
    FROM demo;
"""
count_rows = """
    SELECT COUNT(*)
    FROM demo;
"""

xy_rows = """
    SELECT COUNT(*)
    FROM demo 
    WHERE x >= 5 AND y >= 5
"""

unique_y = """
    SELECT COUNT(DISTINCT(y))
    FROM demo
"""

if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    #execute_query(curs, create_statement)
    execute_query(curs, insert_statement)
    results = execute_query(curs, get_rows)
    results1 = execute_query(curs, count_rows)
    results2 = execute_query(curs, xy_rows)
    results3 = execute_query(curs, unique_y)
    print(results)
    print(results1)
    print(results2)
    print(results3)
