from enum import Enum


class State(Enum):
    """
    Bot state
    """
    STOP = "Stopped"
    RUN = "Running"
    RELOAD = "Reload"
