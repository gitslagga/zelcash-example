## zelcash-example

#### Building for Linux from source
* sudo apt-get update && sudo apt-get upgrade -y
* sudo apt-get install build-essential pkg-config libc6-dev m4 g++-multilib autoconf libtool ncurses-dev unzip git python python-zmq zlib1g-dev wget curl bsdmainutils automake
* git clone https://github.com/zelcash/zelcash.git
* cd zelcash
* git checkout master
* ./zcutil/build.sh -j$(nproc)
* cd zelcash

#### Configuration Zelcash
* mkdir ~/.zelcash
* echo "rpcuser=username" >> ~/.zelcash/zelcash.conf
* echo "rpcpassword=`head -c 32 /dev/urandom | base64`" >> ~/.zelcash/zelcash.conf
* echo "rpcallowip=127.0.0.1" >> ~/.zelcash/zelcash.conf
* echo "addnode=explorer.zel.cash" >> ~/.zelcash/zelcash.conf
* echo "addnode=explorer.zel.zelcore.io" >> ~/.zelcash/zelcash.conf
* ./zcutil/fetch-params.sh
  
#### Run zelcashd
* ./src/zelcashd
* ./src/zelcashd -daemon
* vim /usr/lib/systemd/system/zelcashd.service
  ```
    [Unit]
    Description=Zelcash Daemon

    [Service]
    Type=simple
    ExecStart=/root/code/zelcash-node/zelcash/src/zelcashd
    Restart=on-failure
    User=root
    Group=root

    [Install]
    WantedBy=multi-user.target
  ```
* systemctl daemon-reload
* systemctl start zelcashd.service

#### Necessary Operator
* ./zelcash-cli getinfo
    ```
    {
    "version": 3030150,
    "protocolversion": 170013,
    "walletversion": 60000,
    "balance": 0.00000000,
    "blocks": 385643,
    "timeoffset": 0,
    "connections": 16,
    "proxy": "",
    "difficulty": 7592.848165456719,
    "testnet": false,
    "keypoololdest": 1563517841,
    "keypoolsize": 101,
    "paytxfee": 0.00000000,
    "relayfee": 0.00000100,
    "errors": ""
    }
    ```
* ./zelcash-cli getblockcount
  ```
  385636
  ```
* ./zelcash-cli getnewaddress
  ```
  t1XufmoM2xCx5EWp48SPw5HAb8o8xLiA3xq
  ```
* ./zelcash-cli getbalance && ./zelcash-cli getbalance "*" 6
  ```
  0.00000000
  0.00000000
  ```
* ./zelcash-cli sendtoaddress "t1bwoNzeJ3ZDA6tn2tsrvdguqeLh7cm7WTi" 0.0001 "donation" "seans outpost" true
  * comment to see https://bitcoin.org/en/developer-reference#sendtoaddress
  ```
  9d53dda88195c46c45fc7118dfeb3c5d90bd1b63e239208862909bc8bf556dd5
  ```
* ./zelcash-cli listtransactions "*" 100 0
  ```
  [
    {
        "account": "",
        "address": "t1XufmoM2xCx5EWp48SPw5HAb8o8xLiA3xq",
        "category": "receive",
        "amount": 1.00000000,
        "vout": 0,
        "confirmations": 3,
        "blockhash": "00000034907220bc841cc49f15682cdddeff5e677e20f052632dd5a938b6f30c",
        "blockindex": 1,
        "blocktime": 1563789347,
        "expiryheight": 385726,
        "txid": "63be2959fff8ba00b381091fd86680d85d5b51365a6f9ee2f575d878d4dce301",
        "walletconflicts": [
        ],
        "time": 1563789329,
        "timereceived": 1563789329,
        "vjoinsplit": [
        ],
        "size": 245
    }
  ]
  ```

#### Unnecessary Operator, Setting Up Your Wallet
* ./zelcash-cli signmessage "t1XufmoM2xCx5EWp48SPw5HAb8o8xLiA3xq" "my message"
  ```
  INVnjyYcLHbWyE/wNX9TGWKp5+Kgkqf8eeDtOR5u/VsYABMHSxRg1KnVWD5CefL75iOe2JEJY9l4FJr//fe4MOY=
  ```
* ./zelcash-cli verifymessage "t1XufmoM2xCx5EWp48SPw5HAb8o8xLiA3xq" "INVnjyYcLHbWyE/wNX9TGWKp5+Kgkqf8eeDtOR5u/VsYABMHSxRg1KnVWD5CefL75iOe2JEJY9l4FJr//fe4MOY=" "my message"
  ```
  true
  ```
* ./zelcash-cli dumpwallet ~/.zelcash/wallet-dump.dat 
  ```
  /home/slagga/.zelcash/wallet-dump.dat
  ```
* ./zelcash-cli importwallet ~/.zelcash/wallet-dump.dat 

* ./zelcash-cli dumpprivkey "t1XufmoM2xCx5EWp48SPw5HAb8o8xLiA3xq"
  ```
  L3TaeHx1uXzqi4qE8THrSQQgADk8kimPCuaFj99bNGG6zBZYbnwJ
  ```
* ./zelcash-cli importprivkey "L3TaeHx1uXzqi4qE8THrSQQgADk8kimPCuaFj99bNGG6zBZYbnwJ"
  ```
  t1XufmoM2xCx5EWp48SPw5HAb8o8xLiA3xq
  ```
* ./zelcash-cli listaddressgroupings
  ```
  [
    [
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
  ]
  ```




