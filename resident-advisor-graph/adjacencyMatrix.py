import sqlite3
import numpy as np

conn = sqlite3.connect("DataBase.db") # or use :memory: to put it in RAM

cursor = conn.cursor()

cursor.execute("""SELECT DISTINCT dj FROM myTable""")
djs = cursor.fetchall()


dic1={} # 0: 'dixon'
dic2={} # 'dixon': 0
k=0
for dj in djs:
    dic1[k]=dj[0]
    dic2[dj[0]]=k
    k+=1
    
M = np.zeros((100, 100))    #adjacency matrix   

cursor.execute("""SELECT DISTINCT title, members_attending, number_of_dj FROM myTable""")
titles = cursor.fetchall()

for event in titles:
    cursor.execute("""SELECT DISTINCT dj FROM myTable WHERE title = ? and members_attending = ? and number_of_dj = ?""", (event[0],event[1], event[2]))
    rows = cursor.fetchall()
    
    for row in rows:
        for row1 in rows:
            a=dic2[row[0]]
            b=dic2[row1[0]]
            M[a][b]+=1   

np.save('adjacencyMatrix', M)
dic=[dic1, dic2]
np.save('dico', dic)

conn.commit()