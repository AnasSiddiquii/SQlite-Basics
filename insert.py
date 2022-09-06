import sqlite3
conn=sqlite3.connect('sqlite.db')

try:
    print()
    print('Start')
    print()

    for i in range (3):
        ins1=" INSERT INTO student2 (Name,Class,Email) values ('Ashish','BCA','scd8055@gmail.com') "
        ins2=" INSERT INTO student2 (Name,Class,Email) values ('Anas','MCA','scd8055@gmail.com') "
        ins3=" INSERT INTO student2 (Name,Class,Email) values ('Amaan','BBA','scd8055@gmail.com') "

    conn.execute(ins1)
    conn.execute(ins2)
    conn.execute(ins3)
    conn.commit()

    print('Inserted')

except:
    print('Error')

finally:
    conn.close()
    print()
    print('End')
    print()