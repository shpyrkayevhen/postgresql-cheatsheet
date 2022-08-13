# https://www.postgresqltutorial.com/postgresql-tutorial
# pip instal psycopg2


# ---------------------------------------------------------------------------------------------------------------------------- #


# --- MAIN SQL QUERIES FOR A DATABASE --- #

# Create database
"""CREATE DATABASE fastapi;"""

# Drop database
"""DROP DATABASE IF EXISTS fastapi;"""


# ---------------------------------------------------------------------------------------------------------------------------- #


# --- MAIN SQL QUERIES FOR A TABLE --- #

# 1: CREATE TABLE (https://www.postgresql.org/docs/current/datatype.html)
"""CREATE TABLE products (
    id SERIAL NOT NULL,
    name CHATACTER VARYING(255) NOT NULL,
    price INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),         
    PRIMARY KEY (id)
);"""

# 2: DROP TABLE FROM DATABASE
"""USING database_name;"""
"""DROP TABLE table_name;"""


# ---------------------------------------------------------------------------------------------------------------------------- #


# --- MAIN SQL QUERIES FOR A COLUMNS IN THE TABLE --- #

# 1: ADD NEW COLUMN INTO TABLE
"""ALTER TABLE IF EXISTS products
   ADD COLUMN is_sale BOOLEAN DEFAULT False;"""

# 2: RENAME COLUMN
"""ALTER TABLE table_name 
   RENAME COLUMN column_name TO new_column_name;"""


# 3: CHANGE COLUMN DATA TYPE
"""ALTER TABLE table_name
   ALTER COLUMN column_name [SET DATA] TYPE new_data_type;"""

# 4: DROP COLUMN FROM TABLE
"""ALTER TABLE IF EXISTS products
   DROP COLUMN price;"""


# ---------------------------------------------------------------------------------------------------------------------------- #


# SELECT ALL DATA FROM TABLE (DEFAULT ORDERING IS ASC but we can use DESC)
"""SELECT * FROM products ORDER BY id ASC;"""

# GET ONLY NAME AND PRICE ALL PRODUCTS
"""SELECT name, price FROM products;"""


# GET ONLY NAME ALL PRODUCTS AND CHANGE COLUMN NAME
"""SELECT name AS product_name FROM products;"""


# FILTER DATA

"""SELECT * FROM products WHERE id = 1;"""
"""SELECT * FROM products WHERE price >= 200;"""
"""SELECT * FROM products WHERE price != 50;"""  # <>
"""SELECT * FROM products WHERE inventory > 0 AND price < 200;"""  # OR
"""SELECT * FROM products WHERE id BETWEEN 1 AND 4;"""  # IN(1, 2, 3, 4)

"""SELECT * FROM products WHERE name = 'Iphone';"""
"""SELECT * FROM products WHERE name LIKE 'TV%';"""  # NOT LIKE /'%s'/'%@%'


# GROUP RESULTS BY ...GET ALL PRODUCTS FROM EXPENSIVE TO CHEAP
"""SELECT * FROM products GROUP BY price DESC"""
"""SELECT * FROM products GROUP BY price DESC, inventory ASC"""
"""SELECT * FROM products WHERE inventory > 500 GROUP BY price DESC"""
# GET THE LATEST PRODUCTS
"""SELECT * FROM products GROUP BY created_at DESC"""


# LIMIT OUTPUT RESULTS. GET FIRS 5 PRODUCTS
"""SELECT * FROM products ORDER BY id LIMIT 5"""

# IF WE WANT TO SKIP SOME ROWS. SKIP FIRST 2 PRODUCTS AND GET THE NEXT 3
"""SELECT * FROM products ORDER BY id LIMIT 3 OFFSET 2"""


# ---------------------------------------------------------------------------------------------------------------------------- #

# --- INSERT ENTRIES INTO TABLE --- #

"""INSERT INTO products (name, price )  
   VALUES             ('Samsung', 800),
                        ('Iphone', 900) RETURNING id;"""  # RETURN ID THIS ADDED ENTRIES(ROWS)


# --- UPDAITING ENTRIES IN THE TABLE --- #

# Update single entrie in table:
"""UPDATE table_name SET price = 252 WHERE id = 5 RETURNING *;"""  # Will return updated product
"""UPDATE table_name SET quantity = 50 WHERE name = 'Iphone' AND price = 950;"""
# Update multiply entrie in table:
"""UPDATE table_name SET is_sale = true WHERE id > 50;"""


# --- DELETE ENTRIES FROM TABLE --- #

# DELETE ENTRIE
"""DELETE FROM products WHERE id = 5;"""
# DELETE ENTRIES AND RETURN IT
"""DELETE FROM products WHERE id = 5 RETURNING *;"""
# DELETE MULTIPLY ENTRIESES
"""DELETE FROM products WHERE inventory = 0;"""

# ---------------------------------------------------------------------------------------------------------------------------- #

# --- INNER/RIGHT/LEFT JOIN --- #
