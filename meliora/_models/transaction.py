"""
- Symbol
    - Coin
- Name
    - Name of coin
- Contract
    - Contract address
- Quantity
    - How many coins are a part of this transaction
- Source
    - Where is this transaction from
- Destination
    - Where is this transaction going
- Price
    - Price per coin at the time of the transaction
- Total
    - Total worth of the transaction, including fees?
- Blockchain
    - Blockchain on which this coin exists
- Fees
    - Fees paid for the transaction
- Link
    - URL link to view transaction like BSCscan or Ethscan
- Date
    - Date of transaction
"""


class Transaction():
    def __init__(self, symbol, qty, src, dst, price, blck, fee, date) -> None:
        self.symbol = symbol
        self.qty = qty
        self.src = src
        self.dst = dst
        self.price = price
        self.blck = blck
        self.fee = fee
        self.date = date
