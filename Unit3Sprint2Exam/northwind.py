import sqlite3


def connect_to_db(db_name = 'northwind_small.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# Part 2
# Top 10 most expensive items
expensive_items = """
    SELECT ProductName, UnitPrice
    FROM Product 
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""

# Age of employee on the day they were hired
employee_birth = """
    SELECT AVG(Date(HireDate) - BirthDate)
    FROM Employee;
"""

# Part 3
# Ten most expensive items and their suppliers
expense_supp = """
    SELECT ProductName, UnitPrice, Supplier.Id, Supplier.CompanyName
    FROM Product 
    JOIN Supplier
    ON Product.Id = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""

# Largest Category
large_cat = """
    SELECT COUNT(Category.Id) AS UniqueProducts, Category.CategoryName
    FROM Category 
    JOIN Product
    ON Product.CategoryId = Category.Id
    GROUP BY CategoryName
    ORDER BY UniqueProducts DESC
    LIMIT 1;
"""

if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, expensive_items)
    results1 = execute_query(curs, employee_birth)
    results2 = execute_query(curs, expense_supp)
    results3 = execute_query(curs, large_cat)
    print('The ten most expensive items are:', results)
    print('The average age of an employee at the time of their hiring is', results1)
    print('The ten most expensive items and their suppliers are:', results2)
    print('The largest category by number of unique products is:', results3)