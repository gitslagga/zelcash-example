from waitress import serve

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

serve(app, host='0.0.0.0', port=8080)



###########################################
# pip install waitress
# python -u waitressRun.py