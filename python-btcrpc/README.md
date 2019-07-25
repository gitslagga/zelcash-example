## Programming with Bitcoin Core

#### Introduction
* sudo pip3.7 install python-bitcoinrpc
* sudo pip3.7 install flask
* sudo pip3.7 install flask-restful
* sudo pip3.7 install requests
* sudo pip3.7 install gevent
* cp package/setting.example.py package/setting.py

#### Run Python SDK
* python3.7 script.py
* env FLASK_APP=script.py flask run
* vim /usr/lib/systemd/system/zelsdk.service
  ```
    [Unit]
    Description=Zelsdk Daemon

    [Service]
    Type=simple
    ExecStart=/usr/local/bin/python3.7 /root/code/zelcash-example/python-btcrpc/script.py
    Restart=on-failure
    User=root
    Group=root

    [Install]
    WantedBy=multi-user.target
  ```
* systemctl start zelsdk.service