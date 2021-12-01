from enum import Enum


class NotificationType(Enum):
    """
    Notification types
    """
    STATUS = 'status'
    WARNING = 'warning'
    STARTUP = 'startup'
