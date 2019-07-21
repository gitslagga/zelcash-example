from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

def getConnection():
    rpc_host = '127.0.0.1'
    rpc_port = '16124'
    rpc_user = 'username'
    rpc_password = 'mS2SZpPCZZVZwSP8EOCyMmGxqFNyPoKSUdiYSpcLVQE='

    return AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))