# 1: pip install psycopg2
import psycopg2
# To get data in a dictionary type
import psycopg2.extras
import config

connection = None

# Connect to db, this function return Object Connect
# and this object has a lots of methods .close(), .commit() .fetchall()
try:
    # the same: connection = psycopg2.connect()
    # whis: automaticly connection.commit() in the end.
    # we manualy connection.clothe() in the end.
    with psycopg2.connect(
        host=config.hostname,
        dbname=config.database,
        user=config.username,
        password=config.password,
        port=config.port
    ) as connection:

        # whis: automaticly cursor.close() in the end.
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:

            cursor.execute("""DROP TABLE IF EXISTS employee""")

            # Create table in our db
            create_script = """CREATE TABLE IF NOT EXISTS employee(
                               id BIGSERIAL NOT NULL PRIMARY KEY,
                               name VARCHAR(50) NOT NULL,
                               salary INT NOT NULL,
                               dept_id VARCHAR(30) 
                            );"""
            # Execute our SQL command
            cursor.execute(create_script)

            # Insert multiple records into table
            insert_script = """INSERT INTO employee(name, salary, dept_id) 
                                            VALUES (%s, %s, %s);"""

            insert_value = [('Mosh', 4700, '2'), ('John', 2500, '1'),
                            ('Luka', 3400, '5'), ('Mira', 5500, '4')]
            for employee in insert_value:
                cursor.execute(insert_script, employee)

            # Update data
            update_script = """UPDATE employee SET salary = salary + salary * 0.5;"""
            cursor.execute(update_script)

            # Delete data
            delete_script = """DELETE FROM employee WHERE name = %s;"""
            delete_record = ('Mira',)
            cursor.execute(delete_script, delete_record)

            # Select data
            cursor.execute("""SELECT * FROM employee;""")
            for employee in cursor.fetchall():
                print(employee['name'], employee['salary'])

except Exception as error:
    print(f'Failed to connect to database. Error type: {error}')

finally:
    if connection is not None:
        connection.close()