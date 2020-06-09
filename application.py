from flask import Flask 
from config import DefaultConfig
from flask import jsonify
from model import *

app = Flask(__name__)
app.config.from_object(DefaultConfig)
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/heroes')
def heroes():
    try:
        items = Hero.query.first()
        print(items.serialize())
        return jsonify(items.serialize())
    except:
        return 'Notworking'


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)