import pandas as pd
import json
from bscscan import BscScan
from meliora.config.config import Configuration
from meliora.persistance.database import session

"""
Class to fetch, process and store transaction data
"""


class Transactions:
    def __init__(self):
        self.config = Configuration()
        self.bsc_api = self.config.bsc_api
        self.test_address = self.config.bsc_address

        # print(self.config.bscscan)
        with BscScan(self.config.bsc_api, asynchronous=False) as client:
            txs = client.get_internal_txs_by_address(
                address=self.test_address, startblock=0, endblock=99999999, sort="asc")

            assert len(txs) > 0

            # Writing transactions to .csv file for testing
            # filename = './data/trans'
            # with open(filename, 'w') as f:
            #   for t in txs:
            #     f.write(json.dumps(t))

            header = ["block_number",
                      "timstamp",
                      "hash",
                      "source",
                      "destination",
                      "value",
                      "contract",
                      "input",
                      "trans_type",
                      "gas",
                      "gas_used",
                      "trace_id",
                      "is_error",
                      "err_code"]

            df = pd.DataFrame(txs)
            df.columns = header
            print(df.columns)
            df.to_sql(name="transactions", con=session.get_bind(),
                      if_exists='append', index=False)
