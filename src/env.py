import os

BTC_ELECTRUM_RPC_URL = os.getenv('ELECTRUM_RPC_URL', 'http://electrs:7000')
LTC_ELECTRUM_RPC_URL = os.getenv('ELECTRUM_RPC_URL', 'http://electrs:7001')
ELECTRUM_RPC_USERNAME = os.getenv('ELECTRUM_RPC_USERNAME', '')
ELECTRUM_RPC_PASSWORD = os.getenv('ELECTRUM_RPC_PASSWORD', '')
BITCOIN_WALLET_SEED = os.getenv('BITCOIN_WALLET_SEED', '')

MONERO_RPC_URL = os.getenv('MONERO_RPC_URL', 'http://monero-wallet-rpc:18082/json_rpc')
MONERO_RPC_USERNAME = os.getenv('MONERO_RPC_USERNAME', '')
MONERO_RPC_PASSWORD = os.getenv('MONERO_RPC_PASSWORD', '')
MONERO_WALLET_SEED = os.getenv('MONERO_WALLET_SEED', '')
MONERO_WALLET_PASSWORD = os.getenv('MONERO_WALLET_PASSWORD', '')
MONERO_WALLET_HEIGHT = os.getenv('MONERO_WALLET_HEIGHT', '')
MONERO_DAEMON_ADDRESS = os.getenv('MONERO_DAEMON_ADDRESS', '')

KRAKEN_API_KEY = os.getenv('KRAKEN_API_KEY', '')
KRAKEN_API_SECRET = os.getenv('KRAKEN_API_SECRET', '')

MAX_NETWORK_FEE_PERCENT = float(os.getenv('MAX_NETWORK_FEE_PERCENT', '5'))
MAX_SLIPPAGE_PERCENT = float(os.getenv('MAX_SLIPPAGE_PERCENT', '0.5'))

BITCOIN_FEE_SOURCE = os.getenv('BITCOIN_FEE_SOURCE', 'https://mempool.space/api/v1/fees/recommended')
BITCOIN_FEE_RATE = os.getenv('BITCOIN_FEE_RATE', 'halfHourFee')
LITECOIN_FEE_SOURCE = os.getenv('LITECOIN_FEE_SOURCE', 'https://litecoinspace.org/api/v1/fees/recommended')
LITECOIN_FEE_RATE = os.getenv('LITECOIN_FEE_RATE', 'halfHourFee')