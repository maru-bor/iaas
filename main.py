from pymongo import MongoClient
from flask import Flask, jsonify, render_template
from flask import request



app = Flask(__name__)

client = MongoClient("mongodb://dev.spsejecna.net:27017")
db = client["webnews"]
coll = db["idnes"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods = ['GET'])
def get_posts():
    post = coll.find({'_id' : 0})
    return post


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
