import sqlite3
conn=sqlite3.connect('sqlite.db')

try:
    print()
    print('Start')
    print()


    data=conn.execute('select * from student2') #limit 2,1: start from2 and show1 data
    print('{:<10} {:<10} {:<10} {:<20}'.format('Id','Name','Class','Email'))
    for n in data:
        print('{:<10} {:<10} {:<10} {:<20}'.format(n[0], n[1], n[2], n[3]))

    print()
    print('Show All')

except:
    print('Error')

finally:
    conn.close()
    print()
    print('End')
    print()