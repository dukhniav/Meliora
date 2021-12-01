from enum import Enum


class TransactionStatus(Enum):
    """
    Transaction status types
    """
    COMPLETED = 'completed'
    PENDING = 'pending'
    CANCELLED = 'cancelled'
    REVERSED = 'reversed'
