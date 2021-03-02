import psycopg2

try:
    
    connection = psycopg2.connect(user="postgres",
                                  password="naval",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE student
          (ID INT PRIMARY KEY     NOT NULL,
          name           TEXT    NOT NULL,
          email         REAL); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    postgres_insert_query = """ INSERT INTO student (ID, name, email) VALUES (%s,%s,%s)"""
    record_to_insert = ('1', 'naval', 'naval@gmail.com')
    cursor.execute(postgres_insert_query, record_to_insert)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")