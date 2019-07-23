from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging, datetime

logging.basicConfig()
logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)

rpc_host = '127.0.0.1'
rpc_port = '16124'
rpc_user = 'username'
rpc_password = 'mS2SZpPCZZVZwSP8EOCyMmGxqFNyPoKSUdiYSpcLVQE='

rpc_connection = AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))

wallet_info = rpc_connection.getinfo()
best_block_hash = rpc_connection.getbestblockhash()
