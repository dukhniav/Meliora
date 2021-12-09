"""Types of run states"""
from enum import Enum

class State(Enum):
    """
    Bot state
    """
    STOP = "stopped"
    RUN = "running"
    RELOAD = "reload"
    EXIT = "exit"
    NEW = "new"
