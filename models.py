from enum import IntEnum, auto

class EventState(IntEnum):
    EVENT_CREATED = 0
    NAME_CREATED = auto()
    TIME_CREATED = auto()
    DESCRIPTION_CREATED = auto()
    CAPACITY_CREATED = auto()
    VISIBILITY_CREATED = auto()
    ORGANIZER_NAME_CREATED = auto()
    ATTENDEES_ADDED = auto()
    EVENT_DONE = auto()

class AttendeeState(IntEnum):
    INVITE_SENT = 0
    INVITE_ACCEPTED = auto()
    INVITE_DECLINED = auto()
    INVITE_MAYBE = auto()
    ATTENDEE_NAMED = auto()
    DONE_PROVIDED = auto()
