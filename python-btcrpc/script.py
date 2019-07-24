from flask import Flask, abort, request, jsonify
from flask.json import JSONEncoder as BaseJSONEncoder
from package import getConnection
from package import sendDingDing

import logging
import json
import threading
import datetime
import decimal
import uuid

app = Flask(__name__)
rpc_connection = getConnection()

###################################### rustful api ################################################
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

    try:
        list_transactions = rpc_connection.listtransactions('*', num, start)
    except Exception as ex:
        app.logger.warning('listtransactions exception: {}'.format(ex))
        return jsonify({'code': 500})
    return jsonify({'code': 0, 'data': list_transactions})

@app.route('/listaddressgroupings', methods=['POST'])
def listaddressgroupings():
    address_groupings = rpc_connection.listaddressgroupings()
    return jsonify({'code': 0, 'data': address_groupings})

###################################### keep heart ################################################
def setInterval(func, sec):
    def funcWrapper():
        setInterval(func, sec)
        func()
    t = threading.Timer(sec, funcWrapper)
    t.start()
    return t

def ping():
    pong = rpc_connection.ping()
    app.logger.warning('ping info: {}'.format(pong))

setInterval(ping, 20)

###################################### fix json format type ################################################
class JSONEncoder(BaseJSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d')
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, uuid.UUID):
            return str(o)
        if isinstance(o, bytes):
            return o.decode("utf-8")
        return super(JSONEncoder, self).default(o)

app.json_encoder = JSONEncoder

if __name__ == '__main__':
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    handler.setLevel(logging.WARNING)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(debug=True)
    