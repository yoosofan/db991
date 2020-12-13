import sqlite3
conn = sqlite3.connect('sp.sqlite')
c = conn.cursor()

r1 = c.execute('select * from s;')
r2 = c.execute('select * from p;')

print('S')
for m1 in r1:
  print(m1)
print('P')
for m1 in r2:
  print(m1)

conn.commit()
c.close()

conn.close()
