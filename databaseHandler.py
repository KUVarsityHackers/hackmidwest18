import sqlite3
from models import EventState

fileName = 'database.db'

def initializeDatabase():
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('''CREATE TABLE events
    (key INTEGER PRIMARY KEY, title TEXT, date TEXT, cap INTEGER, creator TEXT, status INTEGER, details TEXT)''')

    c.execute('''CREATE TABLE attendee
    (key INTEGER PRIMARY KEY, name TEXT, phone TEXT, eventID INTEGER, status TEXT)''')

def createEvent(creator):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('''INSERT INTO events (creator) VALUES ({c}, {s})'''
            .format(c = creator, s = EventState.EVENT_CREATED))
    except:
        print("Error creating event")

def nameEvent(name):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    
    