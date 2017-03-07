#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:09:51 2016

@author: BenStanou
"""
from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup


html_doc = """
<html>
    <head>
    <title>Titre de votre site</title>
    <a href="dfdkf" ten="londres">London</a>
    </head>
    <body>
        <a href="/guide/uk/london" con="londres">London</a>
        <p Property="og:title" Content="Weather Winter">Texte à lire 1</p>
        <p prop="autre chose" content="pas ca">Texte à lire 2</p>
    </body>
</html>
"""

sock = urlopen("https://www.residentadvisor.net/event.aspx?892426")
HTMLSource = sock.read().decode('utf-8')
sock.close()
soup = BeautifulSoup(HTMLSource, 'html.parser')

    
def printLinks(list):
    i=0
    while i < len(list):
        print(list[i])
        i+=1
        
def afficherDJ(str1): #with url of event of the year 2016 for a dj
    s=""
    for i in range(35, len(str1)-14):
        s+=str1[i]
    return s
           
def tagLinkOfDJ(tag):
    return tag.has_attr('href') and tag.has_attr('class') and tag.get('href').find("/dj/")>-1 and tag.get('class')[0].find("fl")>-1
 
def tagLinkOfEvent(tag):
    return tag.has_attr('href') and tag.has_attr('itemprop') and tag.get('itemprop').find("url summary")>-1 and tag.get('href').find("/event")>-1

def getListOfEvent(url):
    list=[]
    sock = urlopen(url)
    HTMLSource = sock.read().decode('utf-8')
    sock.close()
    soup = BeautifulSoup(HTMLSource, 'html.parser')
    for tag in soup.find_all(tagLinkOfEvent):
        absoluteURL=parse.urljoin(url, tag.get('href'))
        list = list + [absoluteURL]
    return list  
 
def getListOfDJ(url):
    list=[]
    sock = urlopen(url)
    HTMLSource = sock.read().decode('utf-8')
    sock.close()
    soup = BeautifulSoup(HTMLSource, 'html.parser')
    for tag in soup.find_all(tagLinkOfDJ):
        absoluteURL=parse.urljoin(url, tag.get('href'))
        URLevents2016=absoluteURL+"/dates?yr=2016" 
        list = list + [URLevents2016]
    return list   
          
def tagNumberOfDJ(tag):
    return tag.has_attr('href') and tag.get('href').find("/dj/")>-1

def tagCity(tag):
    return tag.has_attr('href') and tag.get('href').find("/guide/")>-1

def tagClub(tag):
    return tag.has_attr('class') and tag.has_attr('title') and tag.has_attr('href')

def tagCountry(tag):
    return tag.has_attr('src') and tag.has_attr('alt') and tag.has_attr('title')

def StrToFloat(str):
    return float(str.replace(',', ''))

def tagMembersAttending(tag):
    return tag.has_attr('id') and tag.has_attr('class') and tag['id']=='MembersFavouriteCount'
    
def eventTitle(soup): #return a string
    try:
        return soup.find(property="og:title").get("content")
    except:
        return
        
def eventMembersAttending(soup):    #return an int
    try:
        str = soup.find(tagMembersAttending).string
        return int(StrToFloat(str))
    except:
        return
        
def eventCountry(soup):
    try:
        return soup.find(tagCountry).get("alt")
    except:
        return
        
def eventClub(soup):
    try:
        return soup.find(tagClub).string
    except:
        return
        
def eventCity(soup):
    try:
        return soup.find(tagCity).string
    except:
        return
    
def eventNumberOfDJ(soup):
    try:
        n=0
        for tag in soup.find_all(tagNumberOfDJ):
            n=n+1
        return n
    except:
        return
    
#try:
#    print(eventTitle(soup))
#    print(eventMembersAttending(soup))
#    print(eventCountry(soup))
#    print(eventClub(soup))
#    print(eventCity(soup))
#    print(eventNumberOfDJ(soup))
#except:
#    print("exception catched")