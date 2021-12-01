from persistance.models import Coin
from persistance.database import session


def main():
    coin = Coin(
        symbol="shib",
        price=0.223
    )

    session.add(coin)  # Add the user
    session.commit()  # Commit the change
    print("works??!?!?!??")
