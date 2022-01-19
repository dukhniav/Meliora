"""
Class to manage the app
"""
import json
from datetime import datetime
from time import time

from web3 import Web3
from meliora.config import Configuration
from meliora.explorers import Ether
from meliora.enums import SupportedExplorers, SupportedWallets, SupportedNetworks
#
# # SQL
# from sqlalchemy import create_engine, select
# from sqlalchemy.orm import sessionmaker, relationship
from meliora.persistance import Portfolio, Wallet, Network, Asset, Transaction
#
# engine = create_engine('sqlite:///meliora.sqlite')
# #
# # Portfolio.wallet = relationship('Wallet', order_by=Wallet.id, back_populates='portfolio')
# # Wallet.chain = relationship('Chain', order_by=Chain.id, back_populates='wallet')
# # Chain.coin = relationship('Coin', order_by=Coin.id, back_populates='chain')
# # Coin.transaction = relationship('Transaction', order_by=Transaction.hash, back_populates='coin')
#
# base.Base.metadata.create_all(engine, checkfirst=True)
# Session = sessionmaker(bind=engine)
# session = Session()


class Worker:
    def __init__(self, config: Configuration):
        self.web3 = None

        # Connect to web3
        provider = SupportedExplorers.ETHEREUM
        self.connect_web3(provider)
        self.config = config


        # Get wallets
        self.portfolios = self.config.PORTFOLIOS
        self.wallets = self.config.WALLETS

        for k, v in self.portfolios.items():
            portfolio = Portfolio(name='k')
            for w in v:
                # address, name
                supported_networks = SupportedNetworks[self.get_wallet_type(w).upper()]
                for n in supported_networks.value:
                    wallet = Wallet(name=w, address=self.wallets.get(w))
                    # TODO: Get network explorers
                    network = Network(name=n, wallet=wallet)
                    txs = self.get_transactions(n.upper(), wallet.address[0])
                    one = True
                    if txs is not None:
                        for tx in txs:
                            t = self.web3.eth.get_transaction(tx.get('hash'))

                            cntr = ''
                            if t['from'] == wallet.address[0]:
                                cntr = t['to']
                            else:
                                cntr = t['from']
                            print(cntr)
                            x = self.web3.eth.contract.abi()
                            # token = self.web3.eth.contract(abi=eth_abi, address=cntr)
                    # print(n, SupportedExplorers[n.upper()].value)
        # for chain, net in SupportedNetworks:
            # for n in chain.value:
            #     print(chain, n)
                # bc = Chain(name=self.get_blockchain())

    def get_transactions(self, network, address):
        if network == SupportedExplorers.ETHEREUM.name:
            print(address)
            ether = Ether(self.config.ETHER_API)
            return ether.get_normal_txs(address)



    def get_wallet_type(self, wallet_name):
        return wallet_name.split('_')[0]

    def temp_setup(self):
        # Get or create portfolio
        portfolio = Portfolio(name="Main")
        # session.add(portfolio)
        # Get or create wallet
        wallet = Wallet(address=self.config.ETHEREUM_1, name='MetaMask', portfolio=portfolio)
        # session.add(wallet)
        bc = Chain(name='Ethereum', wallet=wallet)
        # session.add(bc)
        coin = Coin(contract='1233456754', name='ADA', chain=bc)
        session.add(coin)
        return coin

    def connect_web3(self, provider: Web3.provider):
        """
        Connect to W3b
        """
        self.web3 = Web3(Web3.HTTPProvider(provider.value))
        print(f'Connected to Web3: {self.web3.isConnected()}')

    def fetch_txs(self, address, coin):
        """
        Fetch transactions from explorer
        """
        txs = self.ether.get_normal_txs(address)
        for tx in txs:
            exists = session.query(Transaction.hash).filter_by(hash=tx.get('hash')).scalar() is not None
            if not exists:
                # TODO: add notification for new transactions
                dt = datetime.utcfromtimestamp(int(tx.get('timeStamp')))
                w3_tx = self.web3.eth.get_transaction(tx.get('hash'))

                transaction = Transaction(
                    wallet=self.config.ETHEREUM_1
                    , hash=tx.get('hash')
                    , from_addr=w3_tx['from']
                    , gas=w3_tx['gas']
                    , gas_price=w3_tx['gasPrice']
                    , nonce=w3_tx['nonce']
                    , to_addr=w3_tx['to']
                    , txs_index=w3_tx['transactionIndex']
                    , value=w3_tx['value']
                    , time_stamp=dt
                    , coin_id=coin.id)
                session.add(transaction)
        session.commit()

    def get_wallets(self):
        """
        Get wallets for bot
        """
        if not self.config.ETHEREUM_1 == '' and self.validate_address(self.config.ETHEREUM_1):
            self.eth_1 = self.config.ETHEREUM_1
        # TODO: save wallet to db

    def validate_address(self, addr: str) -> bool:
        """
        Check if given address is valid
        """
        status = self.web3.isChecksumAddress(addr)
        return status

    def fetch_balance(self, addr):
        """
        Get balance for current wallet
        """
        balance = self.web3.eth.get_balance(addr)
        usd_value = self.web3.fromWei(balance, 'ether')
        print(usd_value)
        print(self.web3.eth.accounts)
        print(self.web3.eth.get_transaction_count(addr))
        abi = json.loads(
            '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_disable","type":"bool"}],"name":"disableTransfers","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"withdrawTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_amount","type":"uint256"}],"name":"destroy","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"transfersEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"newOwner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint8"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_token","type":"address"}],"name":"NewSmartToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Issuance","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Destruction","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_prevOwner","type":"address"},{"indexed":false,"name":"_newOwner","type":"address"}],"name":"OwnerUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')

        contr = self.web3.eth.contract(address='0xD533a949740bb3306d119CC777fa900bA034cd52', abi=abi)
        balance = contr.functions.balanceOf(addr).call()
        print(f'Curve balance: {self.web3.fromWei(balance, "ether")} r')

    def fetch_accounts(self):
        print('ss')
