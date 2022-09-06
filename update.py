import sqlite3
conn=sqlite3.connect('sqlite.db')

try:
    print()
    print('Start')
    print()

    Name=input('Enter name:-')
    conn.execute("UPDATE student1 SET Name= '"+Name+"' where Id=3")
    conn.execute("UPDATE student1 SET Name= '', Class='BCA' where Id=4")
    conn.execute("UPDATE student1 SET Name= 'Iqra', Class= 'BCA', Email= 'xyz' where Id=5")
    conn.commit()

    print()
    print('Updated')

except:
    print('Error')

finally:
    conn.close()
    print()
    print('End')
    print()