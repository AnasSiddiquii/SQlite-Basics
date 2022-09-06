import sqlite3
conn=sqlite3.connect('sqlite.db')

try:
    print()
    print('Start')
    print()

    for i in range (3):
        name=input('Enter name:-')
        data=conn.execute("select * from student1 where Name= '"+name+"' ")
        print('{:<10} {:<10} {:<10} {:<20}'.format('Id','Name','Class','Email'))
        for n in data:
            print('{:<10} {:<10} {:<10} {:<20}'.format(n[0], n[1], n[2], n[3]))

    print()
    print('Found')

except:
    print('Error')

finally:
    conn.close()
    print()
    print('End')
    print()