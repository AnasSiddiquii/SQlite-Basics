import sqlite3
conn=sqlite3.connect('sqlite.db')

try:
    print()
    print('Start')
    print()

    table4='''
            CREATE TABLE Student4 (
                Id INTEGER PRIMARY KEY AutoIncrement,
                Name varchar(50),
                Class varchar(10),
                Email varchar(30)
            )
        '''
    table5='''
                CREATE TABLE Student5 (
                    Id INTEGER PRIMARY KEY AutoIncrement,
                    Name varchar(50),
                    Class varchar(10),
                    Email varchar(30)
                )
            '''
    table6='''
                CREATE TABLE Student6 (
                    Id INTEGER PRIMARY KEY AutoIncrement,
                    Name varchar(50),
                    Class varchar(10),
                    Email varchar(30)
                )
            '''

    conn.execute(table4)
    conn.execute(table5)
    conn.execute(table6)
    print('Saved')

except:
    print('Already Exists')

finally:
    conn.close()
    print()
    print('End')
    print()