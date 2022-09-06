import sqlite3
conn=sqlite3.connect('sqlite.db')

try:
    print()
    print('Start')
    print()


    print('{:<10} {:<10} {:<10} {:<20}'.format('Id','Name','Class','Fees'))
    # data=conn.execute('select b.id,a.name,a.class,b.email from student2 as a inner join student3 as b on a.id=b.name') # way 1 - inner join - same
    
    data=conn.execute('select * from student3 as a inner join student2 as b on a.id=b.id') # way 2 - same

    # data=conn.execute('select * from student3 as a left join student2 as b on a.id=b.id') # way 3 - left join

    for n in data:
        # print(n) # for tuple
        
        # print('{:<10} {:<10} {:<10} {:<20}'.format(n[0], n[1], n[2], n[3]))
        # way 1 - inner join - same
        
        print('{:<10} {:<10} {:<10} {:<20}'.format(n[0], n[5], n[6], n[3]))
        # way 2 - inner join - same

        # print('{:<10} {:<10} {:<10} {:<20}'.format(n[0], n[1], n[2], n[3]))
        # way 3 - left join - only for left elements

    print()
    print('Show All')

except:
    print('Error')

finally:
    conn.close()
    print()
    print('End')
    print()