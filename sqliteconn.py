import sqlite3
conn=sqlite3.connect('sqlite.db')

try:
    print()
    print('Start')
    print()

    table1='''
            CREATE TABLE Student1 (
                Id INTEGER PRIMARY KEY AutoIncrement,
                Name varchar(50),
                Class varchar(10),
                Email varchar(30)
            )
        '''
    table2='''
            CREATE TABLE Student2 (
                Id INTEGER PRIMARY KEY AutoIncrement,
                Name varchar(50),
                Class varchar(10),
                Email varchar(30)
            )
        '''
    table3='''
            CREATE TABLE Student3 (
                Id INTEGER PRIMARY KEY AutoIncrement,
                Name varchar(50),
                Class varchar(10),
                Email varchar(30)
            )
        '''

    conn.execute(table1)
    conn.execute(table2)
    conn.execute(table3)
    print('Saved')

except:
    print('Already Exists')

finally:
    conn.close()
    print()
    print('End')
    print()