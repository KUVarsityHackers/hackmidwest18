from enum import IntEnum, auto

class EventState(IntEnum):
    EVENT_CREATED = 0
    NAME_CREATED = auto()
    TIME_CREATED = auto()
    DESCRIPTION_CREATED = auto()
    CAPCITY_CREATED = auto()
    VISIBILITY_CREATED = auto()
    ORGANIZER_NAME_CREATED = auto()
    ATTENDEES_ADDED = auto()
    EVENT_DONE = auto()

class AttendeeState(IntEnum):
    UNKNOWN = 0
    DECLINED = auto()
    MAYBE = auto()
    ACCEPTED = auto()