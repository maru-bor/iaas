from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = int(os.getenv("MONGO_PORT", "27017"))
mongo_db = os.getenv("MONGO_DB", "webnews")
mongo_collection = os.getenv("MONGO_COLLECTION", "idnes")

mongo_uri = f"mongodb://{mongo_host}:{mongo_port}"

client = MongoClient(mongo_uri)
db = client[mongo_db]
coll = db[mongo_collection]


@app.route('/')
def index():
    posts = list(coll.find({}, {'_id': 0}).sort("date", -1).limit(10))
    return render_template('index.html', posts=posts)


@app.route('/post', methods=['GET'])
def get_posts():
    posts = list(coll.find({}, {'_id': 0}))
    return jsonify(posts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
