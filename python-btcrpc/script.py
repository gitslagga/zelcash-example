from package.bitcoinrpc import *
import logging

rpc_connection = getConnection()

logging.basicConfig()
logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)

best_block_hash = rpc_connection.getbestblockhash()
wallet_info = rpc_connection.getinfo()
