import sqlite3
from models import EventState

fileName = 'database.db'

def initializeDatabase():
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('''CREATE TABLE events
    (key INTEGER PRIMARY KEY, title TEXT, date TEXT, cap INTEGER, visibility INTEGER, creator TEXT, creatorName TEXT, status INTEGER, details TEXT)''')

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
        c.execute('UPDATE events SET title = {n} AND status = {ns} WHERE creator = {c} AND status = {os}'
            .format(n = name, c = creator, os = EventState.EVENT_CREATED, ns = EventState.NAME_CREATED))
        return True
    except:
        return False

def setDatetimeEvent(creator, datetime):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET date = {d} AND status = {ns} WHERE creator = {c} AND status = {os}'
            .format(d = datetime, c = creator, os = EventState.NAME_CREATED, ns = EventState.TIME_CREATED))
        return True
    except:
        return False

def setDescriptionEvent(creator, description):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET description = {d} AND status = {ns} WHERE creator = {c} AND status = {os}'
            .format(d = description, c = creator, os = EventState.TIME_CREATED, ns = EventState.DESCRIPTION_CREATED))
        return True
    except:
        return False

def setCapEvent(creator, cap):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET cap = {p} AND status = {ns} WHERE creator = {c} AND status = {os}'
            .format(p = cap, c = creator, os = EventState.DESCRIPTION_CREATED, ns = EventState.CAPACITY_CREATED))
        return True
    except:
        return False

def setVisibilityEvent(creator, visibility):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET visibility = {a} AND status = {ns} WHERE creator = {c} AND status = {os}'
            .format(a = visibility, c = creator, os = EventState.CAPACITY_CREATED, ns = EventState.VISIBILITY_CREATED))
        return True
    except:
        return False

def setCreatorNameEvent(creator, name):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET creatorName = {n} AND status = {ns} WHERE creator = {c} AND status = {os}'
            .format(n = name, c = creator, os = EventState.VISIBILITY_CREATED, ns = EventState.ORGANIZER_NAME_CREATED))
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