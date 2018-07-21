from enum import IntEnum, auto

class EventState(IntEnum):
    EVENT_CREATED = 0
    NAME_CREATED = auto()
    TIME_CREATED = auto()
    DESCRIPTION_CREATED = auto()
    VISIBILITY_CREATED = auto()
    CAPCITY_CREATED = auto()
    ORGANIZER_NAME_CREATED = auto()
    ADDING_ATTENDEES = auto()
    EVENT_DONE = auto()

