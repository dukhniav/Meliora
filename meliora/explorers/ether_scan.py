'''
Class to intergrate with Ethereum network
'''

from etherscan import Etherscan


class Ether:
    def __init__(self, api_key: str):
        self.ether = Etherscan(api_key)

    def get_balance(self, addr):
        return self.ether.get_eth_balance(address=addr)

    def get_normal_txs(self, addr):
        txs = self.ether.get_normal_txs_by_address(address=addr, startblock=0, endblock=99999999, sort='asc')
        return txs
