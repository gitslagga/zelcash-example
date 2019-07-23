## Zel Restful Api

#### getinfo
* curl -X POST -H 'Content-Type: application/json'  http://localhost:5000/getinfo
* description
  * Returns an object containing various state info.
* request 
  * no parameter
* response
  ```
    {
        "code": 0, 
        "data": {
            "balance": 9.99879789, 
            "blocks": 386296, 
            "connections": 16, 
            "difficulty": 5816.604707838102, 
            "errors": "", 
            "keypoololdest": 1563517841, 
            "keypoolsize": 101, 
            "paytxfee": 0E-8, 
            "protocolversion": 170013, 
            "proxy": "", 
            "relayfee": 0.00000100, 
            "testnet": false, 
            "timeoffset": 0, 
            "version": 3030150, 
            "walletversion": 60000
        }
    }
  ```

#### getblockcount
* curl -X POST   http://localhost:5000/getblockcount
* description
  * Returns the number of blocks in the best valid block chain.
* request
  * no parameter
* response
  ```
    {
        "code": 0, 
        "data": 386302
    }
  ```
  
#### getnewaddress
* curl -X POST -H 'Content-Type: application/json'  http://localhost:5000/getnewaddress
* description
  * Returns a new Zcash address for receiving payments.
* request 
  * no parameter
* response
  ```
    {
        "code": 0, 
        "data": "t1RqbcVDZVT5MthA2d6HYog2wQK4NAhxBXa"
    }
  ```

#### getbalance
* curl -X POST -H 'Content-Type: application/json'  http://localhost:5000/getbalance
* description
  * Returns the server's total available balance.
* request 
  * no parameter
* response
  ```
    {
        "code": 0, 
        "data": 9.99877789
    }
  ```

#### sendtoaddress
* curl -X POST -H 'Content-Type: application/json'  http://localhost:5000/sendtoaddress -d '{"address": "t1bwoNzeJ3ZDA6tn2tsrvdguqeLh7cm7WTi", "amount": "0.00001"}'
* description
  * Send an amount to a given address. The amount is a real and is rounded to the nearest 0.00000001.
* request 
  * address: received payment address, amount: transfer number
* response
  ```
    {
        "code": 0, 
        "data": "73f3bbd6d6207da9af5bee86e0f4280240055830914c555d3e6456297531f569"
    }
  ```

#### listtransactions
* curl -X POST -H 'Content-Type: application/json'  http://localhost:5000/listtransactions -d '{"start": 0, "num": 100}'
* description
  * Returns up to 'count' most recent transactions skipping the first 'from' transactions for account 'account'.
* request 
  * start: transaction start number, num: transaction list number
* response
  * response parameters description, please see https://zcash-rpc.github.io/listtransactions.html
  ```
    {
        "code": 0, 
        "data": [
            {
                "account": "", 
                "address": "t1bwoNzeJ3ZDA6tn2tsrvdguqeLh7cm7WTi", 
                "amount": -0.00001000, 
                "blockhash": "0000000086e515c2e2c27aeac0e3aed7223b6ff13a362470ce0a3676cd10dfc9", 
                "blockindex": 1, 
                "blocktime": 1563863984, 
                "category": "send", 
                "confirmations": 11, 
                "expiryheight": 386339, 
                "fee": -0.00000244, 
                "size": 244, 
                "time": 1563863885, 
                "timereceived": 1563863885, 
                "txid": "73f3bbd6d6207da9af5bee86e0f4280240055830914c555d3e6456297531f569", 
                "vjoinsplit": [], 
                "vout": 0, 
                "walletconflicts": []
            }, 
            {
                "account": "", 
                "address": "t1bwoNzeJ3ZDA6tn2tsrvdguqeLh7cm7WTi", 
                "amount": -0.00001000, 
                "blockhash": "000000285e412adf6e1ea26f0d721feaca9c00bf1a226a752fc7748c37d8eb50", 
                "blockindex": 9, 
                "blocktime": 1563864353, 
                "category": "send", 
                "confirmations": 7, 
                "expiryheight": 386343, 
                "fee": -0.00000245, 
                "size": 244, 
                "time": 1563864100, 
                "timereceived": 1563864100, 
                "txid": "83881154835a9abd6903e7288e6c61f60c9cad9c9ab348c36c2adb84a8905d9e", 
                "vjoinsplit": [], 
                "vout": 1, 
                "walletconflicts": []
            }
        ]
    }
  ```

#### listaddressgroupings
* curl -X POST -H 'Content-Type: application/json'  http://localhost:5000/listaddressgroupings
* description
  * Lists groups of addresses which have had their common ownership
  * made public by common use as inputs or as the resulting change in past transactions
* request 
  * no parameter
* response
  ```
    {
        "code": 0, 
        "data": [
            [
            [
                "t1eFaxULNXcUb3r2qoY9SHvqZKLAXrYDsQ4", 
                0E-8
            ]
            ], 
            [
            [
                "t1aiRJcvJkgV6epZFpCzhoD2diWb2D3wn12", 
                0E-8
            ]
            ]
        ]
    }
  ```



#### Note
* minimal transfer is 0.00001