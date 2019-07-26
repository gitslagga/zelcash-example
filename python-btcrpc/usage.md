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
                "category": "send",
                "amount": -0.00000755,
                "vout": 0,
                "fee": -0.00000245,
                "confirmations": 23,
                "blockhash": "000000203466074f44d888edbefb86475e7127cf5a4458b687fb975728c4ec69",
                "blockindex": 2,
                "blocktime": 1564116413,
                "expiryheight": 388425,
                "txid": "4e2d436da905f7ab6578b1789314118dc39ee6d49d9b3557a7ea5f0a7b76297c",
                "walletconflicts": [
                ],
                "time": 1564116383,
                "timereceived": 1564116383,
                "comment": "donation",
                "to": "seans outpost",
                "vjoinsplit": [
                ],
                "size": 245
            },
            {
                "account": "",
                "address": "t1aYc1LRDbrY721QAXCokAxbSm5extXD4rz",
                "category": "receive",
                "amount": 0.00001000,
                "vout": 0,
                "confirmations": 8,
                "blockhash": "00000020197124844c20a4fedd07ac9f58b882e9fa5c8c8d897d6efcdad908db",
                "blockindex": 1,
                "blocktime": 1564117822,
                "expiryheight": 388448,
                "txid": "b2202b0350381082366ba682a4e4de30577bb11626ea94051201ca670f17019f",
                "walletconflicts": [
                ],
                "time": 1564117771,
                "timereceived": 1564117771,
                "vjoinsplit": [
                ],
                "size": 540
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

#### getblock
* curl -X POST -H 'Content-Type: application/json'  http://localhost:5000/getblock -d '{"hash": "0000000f5a3e8ff57ad1b4fe480b7289246000447c2ae19e84e140ca1974e0b7"}'
* curl -X POST -H 'Content-Type: application/json'  http://localhost:5000/getblock -d '{"height": "388425"}'
* description
  * getblock "hash|height" ( verbosity )
* request 
  * hash: block hash id, height: block chain height
* response
  ```
    {
        "code": 0, 
        "data": {
            "anchor": "2240fa6436fae5945ffe95500c38789f9c10a4e3492e59248b42a75e50ab71b1",
            "bits": "1d4b9d70",
            "chainwork": "00000000000000000000000000000000000000000000000000002298ead20dc2",
            "confirmations": 27,
            "difficulty": 6933.638401260498,
            "finalsaplingroot": "329836ece77ed9d2419f6d1cd7a3d85b67101f0566aac82c9b92a71009549598",
            "hash": "0000000f5a3e8ff57ad1b4fe480b7289246000447c2ae19e84e140ca1974e0b7",
            "height": 388425,
            "merkleroot": "3cae3cd9644f1a310a89626667628642508da24a6fda6aa3cc45423ce3afd952",
            "nextblockhash": "0000001b8f5b0291622e81fc54e8383acdcd0192aef2ef0e68214179bd455cdb",
            "nonce": "007e8d8c00000000000000000000000000000000000000000000000065090000",
            "previousblockhash": "00000004d987cadd5f543d0c4ceb1ed7ed1630fcab84e0cf5abace120068c016",
            "size": 432,
            "solution": "1fa2feb0b3c79555d57764d74a79f662782f009ac959af88fcc12d1faf5db3d54396a55fd6347d944fa46c83d2acde4df3470a53",
            "time": 1564118107,
            "tx": [
            "3cae3cd9644f1a310a89626667628642508da24a6fda6aa3cc45423ce3afd952"
            ],
            "valuePools": [
            {
                "chainValue": 213926.92091852,
                "chainValueZat": 21392692091852,
                "id": "sprout",
                "monitored": true,
                "valueDelta": 0,
                "valueDeltaZat": 0
            },
            {
                "chainValue": 283724.64841566,
                "chainValueZat": 28372464841566,
                "id": "sapling",
                "monitored": true,
                "valueDelta": 0,
                "valueDeltaZat": 0
            }
            ],
            "version": 4
        }
    }
  ```

#### gettransaction
* curl -X POST -H 'Content-Type: application/json'  http://localhost:5000/gettransaction -d '{"txid": "4e2d436da905f7ab6578b1789314118dc39ee6d49d9b3557a7ea5f0a7b76297c"}'
* description
  * Get detailed information about in-wallet transaction <txid>
* request 
  * txid: transaction hash id
* response
  ```
    {
        "code": 0, 
        "data": {
            "amount": -0.00000755,
            "fee": -0.00000245,
            "confirmations": 38,
            "blockhash": "000000203466074f44d888edbefb86475e7127cf5a4458b687fb975728c4ec69",
            "blockindex": 2,
            "blocktime": 1564116413,
            "expiryheight": 388425,
            "txid": "4e2d436da905f7ab6578b1789314118dc39ee6d49d9b3557a7ea5f0a7b76297c",
            "walletconflicts": [
            ],
            "time": 1564116383,
            "timereceived": 1564116383,
            "comment": "donation",
            "to": "seans outpost",
            "vjoinsplit": [
            ],
            "details": [
                {
                "account": "",
                "address": "t1bwoNzeJ3ZDA6tn2tsrvdguqeLh7cm7WTi",
                "category": "send",
                "amount": -0.00000755,
                "vout": 0,
                "fee": -0.00000245,
                "size": 245
                }
            ],
            "hex": "0400008085202f8901b80b8e6cf71e8835769c796eb186cd6899c54b9ecd18b3080b5b01edb22c10f4010000006b483045022100d158c22bc361233fadb17d1a6893618ed1773fa8d43ce188a94e407a3ed22d88022022b59e3db0164916a89e79c224fcdb94aa58590257cfe65ca075414f7e67d86a0121035d53a6466820cc69bbcd7828022bc6a12269b3764e615da9088f0c32a1e7ddf8feffffff02f3020000000000001976a914c63d6c0966ed0f6b7332081e3f1c61c96d2bbc8f88aca8b0f305000000001976a914c117f752d7ed096281499d675a5811c3609655a388ac2aed050049ed05000000000000000000000000"
        }
    }
  ```



#### Note
* minimal transfer is 0.00001
* listtransactions api need judgement category = receive and confirmations > 1, then the address is mapping user flag 
* getTransaction api need txid in wallet