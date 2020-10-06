
import sqlite3 




def connect_to_db(db_name = 'rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# 1. How many characters are there?

GET_CHARACTERS = """
    SELECT * 
    FROM charactercreator_character;
"""

# 2. How many of each specific subclass?

SUBCLASS = """

"""

# 3. How many total Items?

ITEMS = """
    SELECT *
    FROM armory_item;
"""

# 4. How many items are weapons? How many are not?

# ITEM_WEAPONS = """
#     SELECT COUNT(DISTINCT item_id) AS items, COUNT(DISTINCT item_ptr_id) AS weapons FROM
#     (SELECT * 
#     FROM armory_item
#     LEFT JOIN armory_weapon
#     ON item_id = item_ptr_id);
# """

ITEM_WEAPONS = """ 
    SELECT * 
    FROM armory_weapon
"""
# 5. How many items does each character have?

ITEM_PER_CHAR = """
    SELECT character_name, COUNT(DISTINCT item_id) FROM
    (SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name
    FROM charactercreator_character AS cc,
    armory_item AS ai, 
    charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id
    AND ai.item_id = cci.item_id)
    GROUP BY 1 ORDER BY 2 DESC
    LIMIT 20;
"""

# 6. How many weapons does each Character have? 

WEAP_PER_CHAR = """
    SELECT character_name, COUNT(DISTINCT item_ptr_id) FROM
    (SELECT cc.character_id, cc.name AS character_name, aw.item_ptr_id
    FROM charactercreator_character AS cc,
    armory_weapon AS aw, 
    charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id
    AND aw.item_ptr_id = cci.item_id)
    GROUP BY 1 ORDER BY 2 DESC
    LIMIT 20;
"""

# 7. How many items does a character have on average? 

ITEM_AVG_CHAR = """
    SELECT AVG(item)
	FROM 
	(SELECT character_name, COUNT(DISTINCT item_id) AS item FROM
    (SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name
    FROM charactercreator_character AS cc,
    armory_item AS ai, 
    charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id
    AND ai.item_id = cci.item_id)
    GROUP BY 1 ORDER BY 2 DESC)
    ;
"""

# 8. How many weapons does each character have on average? 

WEAP_AVG_CHAR = """
    SELECT AVG(weap) FROM
    (SELECT character_name, COUNT(DISTINCT item_ptr_id) AS weap FROM
    (SELECT cc.character_id, cc.name AS character_name, aw.item_ptr_id
    FROM charactercreator_character AS cc,
    armory_weapon AS aw, 
    charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id
    AND aw.item_ptr_id = cci.item_id)
    GROUP BY 1 ORDER BY 2 DESC)
    ;
"""

if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, GET_CHARACTERS)
    results_items = execute_query(curs, ITEMS)
    results_weapon = execute_query(curs, ITEM_WEAPONS)
    results_item_char = execute_query(curs, ITEM_PER_CHAR)
    results_weapon_char = execute_query(curs, WEAP_PER_CHAR)
    results_avg_item = execute_query(curs, ITEM_AVG_CHAR)
    results_avg_weap = execute_query(curs, WEAP_AVG_CHAR)

    print('1. There are',len(results),'characters')
    print('3. There are', len(results_items), 'items.')
    print('4. There are', (len(results_items) - len(results_weapon)), 'items, and', len(results_weapon), 'weapons')
    print('5. The first 20 rows are:', results_item_char)
    print('6. The first 20 rows are:', results_weapon_char)
    print('7. Characters have an average of', results_avg_item, 'items in their inventory')
    print('8. Characters have an average of', results_avg_weap, 'weapons in their inventory')

