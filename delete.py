import sqlite3
conn=sqlite3.connect('sqlite.db')

try:
    print()
    print('Start')
    print()

    for i in range (3):
        id=input('enter id :-')
        conn.execute('DELETE FROM student1 where Id='+id)
        conn.commit()

    print()
    print('Deleted')

except:
    print('Error')

finally:
    conn.close()
    print()
    print('End')
    print()