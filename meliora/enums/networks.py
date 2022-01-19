"""Types of supported networks"""
from enum import Enum


class SupportedNetworks(Enum):
    """
    Supported networks for wallets
    """
    METAMASK = ['ethereum', 'bsc', 'matic']
    PHANTOM = ['solana']
    # MATIC
    # AVALANCHE
    # SOLANA

