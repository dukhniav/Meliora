from enum import Enum


class Reward(Enum):
    """
    Reward types
    """
    STAKE = 'stake'
    MINE = 'mine'
    AIRDROP = 'airdrop'
    FARMING = 'farming'
    YIELD = 'yield'
    LOYALTY = 'loyalty'
    GAMING = 'gaming'
    QUESTIONNAIRE = 'questionnaire'