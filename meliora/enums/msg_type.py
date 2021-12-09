"""Types of message types"""
from enum import Enum

class MsgType(Enum):
    """
    Bot state messages
    """
    RUN = "Meliora bot is running"
    STOP = "Meliora bot is stopped"
    RELOAD = "Reloading config"
