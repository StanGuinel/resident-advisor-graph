from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup
import crawler as cr
import sqlite3
 
conn = sqlite3.connect("DataBase.db") # or use :memory: to put it in RAM

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS myTable(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     dj TEXT,
     title TEXT,
     country TEXT,
     city TEXT,
     club TEXT,
     members_attending INTEGER,
     number_of_dj INTEGER
)
""")

url="https://www.residentadvisor.net/dj-100.aspx"
list1 = cr.getListOfDJ(url)

for artist in list1:
    
    list2 = cr.getListOfEvent(artist)
    dj = cr.afficherDJ(artist)
 
    for event in list2:
    
        sock = urlopen(event)
        HTMLSource = sock.read().decode('utf-8')
        sock.close()
        soup = BeautifulSoup(HTMLSource, 'html.parser')
        
        data = {"dj" : dj, "title" : cr.eventTitle(soup), 
            "country" :  cr.eventCountry(soup),"city" : cr.eventCity(soup), 
            "club" :  cr.eventClub(soup), "members_attending" :  cr.eventMembersAttending(soup),
            "number_of_dj" : cr.eventNumberOfDJ(soup)}
        cursor.execute("""
                       INSERT INTO myTable(dj, title, country, city, club, members_attending, number_of_dj)
                       VALUES(:dj, :title, :country, :city, :club, :members_attending, :number_of_dj)""", data)


conn.commit()







