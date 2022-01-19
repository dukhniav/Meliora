"""Types of supported block explorers"""
from enum import Enum


class SupportedExplorers(Enum):
    """
    Supported block explorers
    """
    ETHEREUM = "https://mainnet.infura.io/v3/db9861dd7b904554bc3e1ce8fb9d44f3"
    BSC = "https://bsc-dataseed.binance.org/"
    SOLANA = ""
    MATIC = ""
    AVALANCHE = ""
