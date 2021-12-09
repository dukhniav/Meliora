# pylint: disable=too-few-public-methods
"""
Class to fetch, process and store transaction data
"""
import pandas as pd
from bscscan import BscScan
from meliora.config.config import Configuration
from meliora.persistance.database import session


class Transactions:
    """
    Class to fetch, process and store transaction data
    """

    def __init__(self):
        self.config = Configuration()
        self.bsc_api = self.config.BSC_API_KEY
        self.test_address = self.config.BSC_ADDRESS

        # print(self.config.bscscan)
        with BscScan(self.config.BSC_API_KEY, asynchronous=False) as client:  # pylint: disable=not-context-manager
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

            dataframe = pd.DataFrame(txs)
            dataframe.columns = header
            print(dataframe.columns)
            dataframe.to_sql(name="transactions", con=session.get_bind(),
                             if_exists='append', index=False)
