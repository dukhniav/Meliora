# pragma pylint: disable=too-few-public-methods

"""
bot constants
"""
from typing import List, Tuple


DEFAULT_CONFIG = 'config.json'
DEFAULT_EXCHANGE = 'bittrex'
PROCESS_THROTTLE_SECS = 5  # sec
HYPEROPT_EPOCH = 100  # epochs
RETRY_TIMEOUT = 30  # sec
TIMEOUT_UNITS = ['minutes', 'seconds']
EXPORT_OPTIONS = ['none', 'trades']
DEFAULT_DB_PROD_URL = 'sqlite:///meliora.sqlite'
DEFAULT_DB_DRYRUN_URL = 'sqlite:///meliora.dryrun.sqlite'
BACKTEST_BREAKDOWNS = ['day', 'week', 'month']
DRY_RUN_WALLET = 1000
DATETIME_PRINT_FORMAT = '%Y-%m-%d %H:%M:%S'
MATH_CLOSE_PREC = 1e-14  # Precision used for float comparisons
DEFAULT_DATAFRAME_COLUMNS = ['date', 'open', 'high', 'low', 'close', 'volume']
# Don't modify sequence of DEFAULT_TRADES_COLUMNS
# it has wide consequences for stored trades files
DEFAULT_TRADES_COLUMNS = ['timestamp', 'id',
                          'type', 'side', 'price', 'amount', 'cost']

LAST_BT_RESULT_FN = '.last_result.json'
FTHYPT_FILEVERSION = 'fthypt_fileversion'

TELEGRAM_SETTING_OPTIONS = ['on', 'off', 'silent']
WEBHOOK_FORMAT_OPTIONS = ['form', 'json', 'raw']

ENV_VAR_PREFIX = 'MELIORA__'

NON_OPEN_EXCHANGE_STATES = ('cancelled', 'canceled', 'closed', 'expired')

# Define decimals per coin for outputs
# Only used for outputs.
DECIMAL_PER_COIN_FALLBACK = 3  # Should be low to avoid listing all possible FIAT's
DECIMALS_PER_COIN = {
    'BTC': 8,
    'ETH': 5,
}

DUST_PER_COIN = {
    'BTC': 0.0001,
    'ETH': 0.01
}

SUPPORTED_FIAT = [
    "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK",
    "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY",
    "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN",
    "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR", "USD",
    "BTC", "ETH", "XRP", "LTC", "BCH"
]

MINIMAL_CONFIG = {
    'stake_currency': '',
    'dry_run': True,
    'exchange': {
        'name': '',
        'key': '',
        'secret': '',
        'pair_whitelist': [],
        'ccxt_async_config': {
            'enableRateLimit': True,
        }
    }
}

SCHEMA_TRADE_REQUIRED = [
    'exchange',
    'timeframe',
    'max_open_trades',
    'stake_currency',
    'stake_amount',
    'tradable_balance_ratio',
    'last_stake_amount_min_ratio',
    'dry_run',
    'dry_run_wallet',
    'ask_strategy',
    'bid_strategy',
    'unfilledtimeout',
    'stoploss',
    'minimal_roi',
    'internals',
    'dataformat_ohlcv',
    'dataformat_trades',
]

SCHEMA_BACKTEST_REQUIRED = [
    'exchange',
    'max_open_trades',
    'stake_currency',
    'stake_amount',
    'dry_run_wallet',
    'dataformat_ohlcv',
    'dataformat_trades',
]

SCHEMA_MINIMAL_REQUIRED = [
    'exchange',
    'dry_run',
    'dataformat_ohlcv',
    'dataformat_trades',
]

CANCEL_REASON = {
    "TIMEOUT": "cancelled due to timeout",
    "PARTIALLY_FILLED_KEEP_OPEN": "partially filled - keeping order open",
    "PARTIALLY_FILLED": "partially filled",
    "FULLY_CANCELLED": "fully cancelled",
    "ALL_CANCELLED": "cancelled (all unfilled and partially filled open orders cancelled)",
    "CANCELLED_ON_EXCHANGE": "cancelled on exchange",
    "FORCE_SELL": "forcesold",
}

# List of pairs with their timeframes
PairWithTimeframe = Tuple[str, str]
ListPairsWithTimeframes = List[PairWithTimeframe]

# Type for trades list
TradeList = List[List]
