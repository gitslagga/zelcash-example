from flask import Flask, abort, request, jsonify
from package import getConnection
from package import sendDingDing

import logging
import json

app = Flask(__name__)
rpc_connection = getConnection()

@app.route('/getinfo', methods=['POST'])
def getinfo():
    wallet_info = rpc_connection.getinfo()
    return jsonify({'code': 0, 'data': wallet_info})

@app.route('/getblockcount', methods=['POST'])
def getblockcount():
    block_count = rpc_connection.getblockcount()
    return jsonify({'code': 0, 'data': block_count})

@app.route('/getnewaddress', methods=['POST'])
def getnewaddress():
    new_address = rpc_connection.getnewaddress()
    return jsonify({'code': 0, 'data': new_address})

@app.route('/getbalance', methods=['POST'])
def getbalance():
    balance = rpc_connection.getbalance()
    return jsonify({'code': 0, 'data': balance})

@app.route('/sendtoaddress', methods=['POST'])
def sendtoaddress():
    app.logger.warning('request params: {}'.format(request.json))

    if not request.json or 'address' not in request.json or 'amount' not in request.json:
        abort(400)
    else:
        try:
            hash = rpc_connection.sendtoaddress(request.json['address'], request.json['amount'])
        except Exception as ex:
            app.logger.warning('Sendtoaddress exception: {}'.format(ex))
            sendDingDing('Sendtoaddress exception: {}, request json: {}'.format(ex, request.json))
            return jsonify({'code': 500})
        return jsonify({'code': 0, 'data': hash})

@app.route('/listtransactions', methods=['POST'])
def listtransactions():
    start = 0
    num = 100

    if request.json and 'start' in request.json:
        start = request.json['start']
    if request.json and 'num' in request.json:
        num = request.json['num']
    
    list_transactions = rpc_connection.listtransactions('*', num, start)
    return jsonify({'code': 0, 'data': list_transactions})

@app.route('/listaddressgroupings', methods=['POST'])
def listaddressgroupings():
    address_groupings = rpc_connection.listaddressgroupings()
    return jsonify({'code': 0, 'data': address_groupings})

if __name__ == '__main__':
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    handler.setLevel(logging.WARNING)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(debug=True)
    