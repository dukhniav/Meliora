"""Types of fiat"""
from enum import Enum


class Fiat(Enum):
    """
    Fiat types
    """
    USD = "usd"
    USDT = "usdt"
    BTC = "btc"
