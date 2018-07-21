import sqlite3
from models import EventState, AttendeeState

fileName = 'database.db'

def initializeDatabase():
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('''CREATE TABLE events
    (key INTEGER PRIMARY KEY, title TEXT, date TEXT, cap INTEGER, visibility INTEGER, creator TEXT, creatorName TEXT, status INTEGER, details TEXT)''')

    c.execute('''CREATE TABLE attendees
    (key INTEGER PRIMARY KEY, name TEXT, phone TEXT, eventID INTEGER, status TEXT)''')

def createEvent(creator):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    if hadUnfinishedEvent(creator):
        return False

    try:
        c.execute('INSERT INTO events (creator, status) VALUES (?, ?)'
            ,(creator,EventState.EVENT_CREATED,))
        return True
    except:
        print("Error creating event")
        return False

def setNameEvent(creator, name):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET title = ? AND status = ? WHERE creator = ? AND status = ?'
            ,[name, EventState.NAME_CREATED, creator, EventState.EVENT_CREATED])
        return True
    except:
        print("Error naming event")
        return False

def setDatetimeEvent(creator, datetime):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET date = ? AND status = ? WHERE creator = ? AND status = ?'
            ,[datetime, EventState.TIME_CREATED, creator, EventState.NAME_CREATED])
        return True
    except:
        print("Error setting date and time for event")
        return False

def setDescriptionEvent(creator, description):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET description = ? AND status = ? WHERE creator = ? AND status = ?'
            ,[description, EventState.DESCRIPTION_CREATED, creator, EventState.TIME_CREATED])
        return True
    except:
        print("Error setting description for event")
        return False

def setCapEvent(creator, cap):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET cap = ? AND status = ? WHERE creator = ? AND status = ?'
            ,[cap, EventState.CAPACITY_CREATED, creator, EventState.DESCRIPTION_CREATED])
        return True
    except:
        print("Error setting cap for event")
        return False

def setVisibilityEvent(creator, visibility):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET visibility = ? AND status = ? WHERE creator = ? AND status = ?'
            ,[visibility, EventState.VISIBILITY_CREATED, creator, EventState.CAPACITY_CREATED])
        return True
    except:
        print("Error defining visibility for event")
        return False

def setCreatorNameEvent(creator, name):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET creatorName = ? AND status = ? WHERE creator = ? AND status = ?'
            ,[name, EventState.ORGANIZER_NAME_CREATED, creator, EventState.VISIBILITY_CREATED])

        c.execute('SELECT key FROM events WHERE creator = ? AND status = ?'
            ,[creator, EventState.ORGANIZER_NAME_CREATED])
        eventID = c.fetchone()[0]

        c.exectue('INSERT INTO attendees (name, phone, eventID, status) VALUES (?, ?, ?, ?,)'
            ,[name, creator, eventID, AttendeeState.ACCEPTED])
        return True
    except:
        print("Error setting the creator name for event")
        return False

def sendInvite(sender, invitee):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()
    eventID = 0

    try:
        c.execute('SELECT eventID FROM attendees WHERE phone = ?'
            ,[sender])
        eventID = c.fetchone()[0]

        c.execute('INSERT INTO attendees (phone, eventID, status) VALUES (?, ?, ?)'
            ,[invitee, eventID, AttendeeState.INVITE_SENT])
        return True
    except:
        print("Error sending invite")
        return False

def hadUnfinishedEvent(creator):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT status FROM events WHERE creator = ?'
        ,[creator])
    createdEvents = c.fetchall()
    for createdEvent in createdEvents:
        if createdEvent and createdEvent != EventState.EVENT_DONE:
            return True
    return False

def getState(phone):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT status FROM events WHERE creator = ?'
        ,[phone])
    createdEvents = c.fetchall()
    for createdEvent in createdEvents:
        if createdEvent and createdEvent < EventState.EVENT_DONE:
            return EventState(createdEvent)
    c.execute('SELECT status FROM attendees WHERE phone = ?'
        ,[phone])
    attendeeEvents = c.fetchall()
    for attendeeEvent in attendeeEvents:
        if attendeeEvent and attendeeEvent < AttendeeState.DONE_PROVIDED:
            return EventState(createdEvent)
    return None
