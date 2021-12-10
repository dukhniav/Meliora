"""Types of run states"""
from enum import Enum


class State(Enum):
    """
    Bot state
    """
    STOPPED = "stopped"
    RUNNING = "running"
    RELOAD = "reload"
    EXIT = "exit"
    NEW = "new"
