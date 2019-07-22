# from package.bitcoinrpc import *
from flask import Flask, abort, request, jsonify

import logging
import json

app = Flask(__name__)

# rpc_connection = getConnection()

# best_block_hash = rpc_connection.getbestblockhash()
# wallet_info = rpc_connection.getinfo()

@app.route('/getinfo', methods=['POST'])
def getinfo():
    return jsonify({'code': 0, 'data': {
        'version': 3030150,
        'protocolversion': 170013,
        'walletversion': 60000,
        'balance': 0.00000000,
        'blocks': 385643,
        'timeoffset': 0,
        'connections': 16,
        'proxy': '',
        'difficulty': 7592.848165456719,
        'testnet': False,
        'keypoololdest': 1563517841,
        'keypoolsize': 101,
        'paytxfee': 0.00000000,
        'relayfee': 0.00000100,
        'errors': ''
    }})

@app.route('/getblockcount', methods=['POST'])
def getblockcount():
    return jsonify({'code': 0, 'data': 385636})

@app.route('/getnewaddress', methods=['POST'])
def getnewaddress():
    return jsonify({'code': 0, 'data': 't1XufmoM2xCx5EWp48SPw5HAb8o8xLiA3xq'})

@app.route('/getbalance', methods=['POST'])
def getbalance():
    return jsonify({'code': 0, 'data':   '0.00000000'})

@app.route('/sendtoaddress', methods=['POST'])
def sendtoaddress():
    app.logger.warning('request params: {}'.format(request.json))

    if not request.json or 'address' not in request.json or 'amount' not in request.json:
        abort(400)
    else:
        try:
            address = request.json['address']
            amount = request.json['amount']
        except Exception as ex:
            app.logger.warning('Sendtoaddress Exception: {}'.format(ex))
            return jsonify({'code': 500})
        return jsonify({'code': 0, 'data': '9d53dda88195c46c45fc7118dfeb3c5d90bd1b63e239208862909bc8bf556dd5'})

@app.route('/listtransactions', methods=['POST'])
def listtransactions():
    start = 0
    end = 100

    if request.json and 'start' in request.json:
        start = request.json['start']
    if request.json and 'end' in request.json:
        end = request.json['end']
        
    return jsonify({'code': 0, 'data': [{
        'account': '',
        'address': 't1XufmoM2xCx5EWp48SPw5HAb8o8xLiA3xq',
        'category': 'receive',
        'amount': 1.00000000,
        'vout': 0,
        'confirmations': 3,
        'blockhash': '00000034907220bc841cc49f15682cdddeff5e677e20f052632dd5a938b6f30c',
        'blockindex': 1,
        'blocktime': 1563789347,
        'expiryheight': 385726,
        'txid': '63be2959fff8ba00b381091fd86680d85d5b51365a6f9ee2f575d878d4dce301',
        'walletconflicts': [ ],
        'time': 1563789329,
        'timereceived': 1563789329,
        'vjoinsplit': [ ],
        'size': 245
    }]})

@app.route('/listaddressgroupings', methods=['POST'])
def listaddressgroupings():
    return jsonify({'code': 0, 'data': [[
        [
            "t1XbeuL2ctQgEg4Kb5QK7EZL4JVXV7Davpb",
            0.99890000
        ], 
        [
            "t1XufmoM2xCx5EWp48SPw5HAb8o8xLiA3xq",
            0.00000000,
            ""
        ],
        [
            "t1eFaxULNXcUb3r2qoY9SHvqZKLAXrYDsQ4",
            0.00000000
        ]
    ],
    [
        [
            "t1fhZSunDvwrf6gNcYNXV26jJ9DcCPdX76W",
            8.99989789,
            ""
        ]
    ]
  ]})

if __name__ == '__main__':
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    handler.setLevel(logging.WARNING)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(debug=True)
    