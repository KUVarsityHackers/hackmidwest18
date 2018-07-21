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

    if hadUnfinishedEvent(creator):
        return False

    try:
        c.execute('INSERT INTO events (creator, status) VALUES ({c}, {s})'
            .format(c = creator, s = EventState.EVENT_CREATED))
        return True
    except:
        print("Error creating event")
        return False

def nameEvent(creator, name):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events WHERE (creator, status) = ({c}, {os}) SET name = {n} AND status = {ns}'
            .format(n = name, c = creator, os = EventState.EVENT_CREATED, ns = EventState.NAME_CREATED))
        return True
    except:
        return False

def hadUnfinishedEvent(creator):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT status FROM events WHERE creator = {c}'
        .format(c = creator))
    createdEvents = c.fetchall()
    for createdEvent in createdEvents:
        if createdEvent and createdEvent != EventState.EVENT_DONE:
            return True
    return False

