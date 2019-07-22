from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from .setting import *

def getConnection():
    return AuthServiceProxy('http://%s:%s@%s:%s'%(RPC_HOST, RPC_PASSWORD, RPC_HOST, RPC_PORT))