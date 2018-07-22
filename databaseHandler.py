import sqlite3
from models import EventState, AttendeeState

fileName = 'database.db'

def initializeDatabase():
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('''CREATE TABLE events
    (key INTEGER PRIMARY KEY, title TEXT, date TEXT, cap INTEGER, visibility INTEGER, creator TEXT, creatorName TEXT, status INTEGER, details TEXT)''')

    c.execute('''CREATE TABLE attendees
    (key INTEGER PRIMARY KEY, name TEXT, phone TEXT, eventID INTEGER, status INTEGER, isOwner BOOLEAN, canAdd BOOLEAN)''')

    closeConnection(conn)

def isOwner(phone,eventID):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT isOwner FROM attendees WHERE eventID = ? AND phone = ?'
        ,[eventID,phone])
    isOwner = c.fetchone()[0]
    closeConnection(conn)

    return isOwner
def canAdd(phone,state):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT canAdd FROM attendees WHERE status = ? AND phone = ?'
        ,[int(state),phone])
    canAdd = c.fetchone()[0]
    closeConnection(conn)

    return canAdd

def createEvent(creator):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    if hadUnfinishedEvent(creator):
        return False

    try:
        c.execute('INSERT INTO events (creator, status) VALUES (?, ?)'
            ,[creator,EventState.EVENT_CREATED])
        closeConnection(conn)
        return True
    except:
        print("Error creating event")
        closeConnection(conn)
        return False

def setNameEvent(creator, name):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET title = ?, status = ? WHERE creator = ? AND status = ?'
            ,[name, int(EventState.NAME_CREATED), creator, int(EventState.EVENT_CREATED)])
        closeConnection(conn)
        return True
    except:
        print("Error naming event")
        closeConnection(conn)
        return False

def setDatetimeEvent(creator, datetime):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET date = ?, status = ? WHERE creator = ? AND status = ?'
            ,[datetime, EventState.TIME_CREATED, creator, EventState.NAME_CREATED])
        closeConnection(conn)
        return True
    except:
        print("Error setting date and time for event")
        closeConnection(conn)
        return False

def setDescriptionEvent(creator, description):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET details = ?, status = ? WHERE creator = ? AND status = ?'
            ,[description, EventState.DESCRIPTION_CREATED, creator, EventState.TIME_CREATED])
        closeConnection(conn)
        return True
    except:
        print("Error setting description for event")
        closeConnection(conn)
        return False

def setCapEvent(creator, cap):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET cap = ?, status = ? WHERE creator = ? AND status = ?'
            ,[cap, EventState.CAPACITY_CREATED, creator, EventState.DESCRIPTION_CREATED])
        closeConnection(conn)
        return True
    except:
        print("Error setting cap for event")
        closeConnection(conn)
        return False

def setVisibilityEvent(creator, visibility):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET visibility = ?, status = ? WHERE creator = ? AND status = ?'
            ,[visibility, EventState.VISIBILITY_CREATED, creator, EventState.CAPACITY_CREATED])
        closeConnection(conn)
        return True
    except:
        print("Error defining visibility for event")
        closeConnection(conn)
        return False

def setCreatorNameEvent(creator, name):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET creatorName = ?, status = ? WHERE creator = ? AND status = ?'
            ,[name, EventState.ORGANIZER_NAME_CREATED, creator, EventState.VISIBILITY_CREATED])

        c.execute('SELECT key FROM events WHERE creator = ? AND status = ?'
            ,[creator, EventState.ORGANIZER_NAME_CREATED])
        eventID = c.fetchone()[0]
        c.execute('INSERT INTO attendees (name, phone, eventID, status, isOwner, canAdd) VALUES (?, ?, ?, ?, ?, ?)', [str(name), creator, int(eventID), int(AttendeeState.DONE_PROVIDED), True, True ])
        closeConnection(conn)
        return True
    except Exception as e:
        print(e)
        print("Error setting the creator name for event")
        closeConnection(conn)
        return False

def sendInvite(sender, invitee):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('SELECT eventID FROM attendees WHERE phone = ? AND NOT status = ?'
            ,[sender, EventState.EVENT_DONE])
        eventID = c.fetchone()[0]

        c.execute('UPDATE events SET status = ? WHERE key = ?', [EventState.ATTENDEES_ADDED, eventID])
        print("UPDATED")
        c.execute('SELECT visibility FROM events WHERE key = ?'
            ,[eventID])
        visibility = c.fetchone()[0]
        print("VISIBILITY")
        print(visibility)
        canAdd = False
        if visibility == 1:
            canADD = False
        elif visibility == 3 or visibility != 2:
            canAdd = True
        else:
            canAdd = isOwner(sender,eventID)
        print("ISOWNERWORKS")
        c.execute('INSERT INTO attendees (phone, eventID, status, isOwner, canAdd) VALUES (?, ?, ?, ?, ?)'
            ,[str(invitee), int(eventID), int(AttendeeState.INVITE_SENT), False, canAdd])
        closeConnection(conn)
        return True
    except Exception as e:
        print(e)
        print("Error sending invite")
        closeConnection(conn)
        return False
def getKeyAttendee(phone_number):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT eventID FROM attendees WHERE phone = ? AND (NOT status = ? OR NOT status = ? OR NOT status = ?)'
        ,[phone_number, AttendeeState.DONE_PROVIDED, AttendeeState.INVITE_DECLINED, AttendeeState.INVITE_MAYBE])
    eventID = c.fetchone()[0]
    closeConnection(conn)
    return eventID
def getPersonName(phone_number):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT creatorName FROM events WHERE creator = ? AND NOT status = ?'
        ,[phone_number, EventState.EVENT_DONE])
    creatorNames = c.fetchone()
    if creatorNames is not None:
        for creatorName in creatorNames:
            if len(creatorName) > 0:
                closeConnection(conn)
                return str(creatorName)
    c.execute('SELECT name FROM attendees WHERE phone = ?'
            ,[phone_number])
    attendeeNames = c.fetchone()

    if attendeeNames is not None:
        for attendeeName in attendeeNames:
            if len(attendeeName) > 0:
                closeConnection(conn)
                return str(attendeeName)
    return None

def getEventDescription(key):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT details FROM events WHERE key = ?'
        ,[key])
    creatorNames = c.fetchone()
    if creatorNames is not None:
        for creatorName in creatorNames:
            if len(creatorName) > 0:
                closeConnection(conn)
                return str(creatorName)
    return None

def getEventTime(key):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT date FROM events WHERE key = ?'
        ,[key])
    creatorNames = c.fetchone()
    if creatorNames is not None:
        for creatorName in creatorNames:
            if len(creatorName) > 0:
                closeConnection(conn)
                return str(creatorName)
    return None

def getOpenEventName(key):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT title FROM events WHERE key = ?'
        ,[key])
    createdEventName = c.fetchone()
    closeConnection(conn)
    if not (createdEventName is None):
        return createdEventName[0]
    return None

def hadUnfinishedEvent(creator):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT status FROM events WHERE creator = ?'
        ,[creator])
    createdEvents = c.fetchall()
    for createdEvent in createdEvents:
        if createdEvent != EventState.EVENT_DONE:
            closeConnection(conn)
            return True
    closeConnection(conn)
    return False

def inviteAccepted(invitee):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE attendees set status = ? WHERE phone = ?'
            ,[AttendeeState.INVITE_ACCEPTED, invitee])
        closeConnection(conn)
        return True
    except:
        print("Error accepting invite")
        closeConnection(conn)
        return False

def inviteDeclined(invitee):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE attendees set status = ? WHERE phone = ?',
            [AttendeeState.INVITE_DECLINED, invitee])
        closeConnection(conn)
        return True
    except:
        print("Error declining invite")
        closeConnection(conn)
        return False

def inviteMaybe(invitee):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE attendees set status = ? WHERE phone = ?',
            [AttendeeState.INVITE_MAYBE, invitee])
        closeConnection(conn)
        return True
    except:
        print("Error responding with maybe")
        closeConnection(conn)
        return False

def setAttendeeName(phone, name):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE attendees set name = ?, status = ? where phone = ?', [name, int(AttendeeState.ATTENDEE_NAMED), phone])
        closeConnection(conn)
        return True
    except:
        print("Error adding attendee name")
        closeConnection(conn)
        return False

def getState(phone):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT status FROM events WHERE creator = ?'
        ,[phone])
    createdEvents = c.fetchone()
    if createdEvents is not None:
        for createdEvent in createdEvents:
            if int(createdEvent) < int(EventState.EVENT_DONE):
                closeConnection(conn)
                return EventState(int(createdEvent))
    c.execute('SELECT status FROM attendees WHERE phone = ?'
            ,[phone])
    attendeeEvents = c.fetchone()

    if attendeeEvents is not None:
        for attendeeEvent in attendeeEvents:
            if int(attendeeEvent) < int(AttendeeState.DONE_PROVIDED):
                closeConnection(conn)
                return AttendeeState(attendeeEvent)
    closeConnection(conn)
    return None

def closeConnection(conn):
    conn.commit()
    conn.close()

def setDone(creator):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('UPDATE events SET status = ? WHERE creator = ? AND status = ?'
            ,[EventState.EVENT_DONE, creator, EventState.ATTENDEES_ADDED])
        closeConnection(conn)
        return True
    except:
        print("Error setting done for event")
        closeConnection(conn)
        return False

def setAttendeeDone(phone_number):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    try:
        c.execute('''UPDATE attendees SET status = ? WHERE phone = ? AND status = ?''', [AttendeeState.DONE_PROVIDED, phone_number, AttendeeState.ATTENDEE_NAMED])
        closeConnection(conn)
        return True
    except:
        print("Failed to move user to done")
        closeConnection(conn)
        return False

def getAlltimes():
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT key, date, creator FROM events')
    keytimes = c.fetchall()
    closeConnection(conn)
    return keytimes

def getAttendees(key):
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT name, phone FROM attendees WHERE key = ?', [key])
    Attendees = c.fetchall()
    closeConnection(conn)
    return Attendees
    

def remind_jobs():
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    c.execute('SELECT(key,date) FROM events')
    return c.fetchall()
