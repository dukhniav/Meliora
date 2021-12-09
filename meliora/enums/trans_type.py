"""Types of transaction types"""
from enum import Enum


class TransactionType(Enum):
    """
    Transaction types
    """
    AUTO = "Auto"
    MANUAL = "Manual"
