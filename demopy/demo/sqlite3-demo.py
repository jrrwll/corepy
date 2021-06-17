import sqlite3 as db

'''
SQL         Python

INTEGER     int
REAL        float
TEXT        str
BLOB        buffer  #Binary Large Object, mp3/jpg...
NULL        None
'''

con = db.connect('first.db')

cur = con.cursor()
cur.execute('CREATE TABLE MyTableName(Region TEXT, Population INTEGER)')

cur.execute('INSERT INTO MyTableName VALUES("China", 330993)')
cur.execute('INSERT INTO MyTableName VALUES("Japan", 40903)')
cur.execute('INSERT INTO MyTableName VALUES("USA", 1030191)')
con.commit()

cur.execute('SELECT  Region Population FROM MyTableName')
con.text_factory = str
# return a tuple included values
print(cur.fetchone())

cur.execute('SELECT Region Population FROM MyTableName ORDER BY Region ASC')
print(cur.fetchall())

cur.execute('UPDATE MyTableName SET Population = 1000 WHERE Region = "Japan"')
cur.execute('DELETE FROM MyTableName WHERE Region = Region > "L"')
cur.execute('DROP TABLE MyTableName')

cur.execute('CREATE TABLE NumAlpha(Num INTEGER, Alpha TEXT)')
cous = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
for c in cous:
    cur.execute('INSERT INTO NumAlpha VALUES(?, ?)', (c[0], c[1]))
con.commit()
