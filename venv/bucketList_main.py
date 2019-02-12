from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask("__name__")

app.config["MONGO_DBNAME"] = "goals"
app.config["MONGO_URI"] = "mongodb://localhost:27017/goals"

mongo = PyMongo(app)

@app.route('/') #to check whether the application is running correctly on port
def hello_world():
    return 'flask is running correctly'

@app.route('/viewBucketList', methods=['GET']) #viewing all contents of bucketList
def get_bucketList():
	bucketList = mongo.db.bucketList
	items = []
	item = bucketList.find()
	for j in item:
		j.pop('_id')
		items.append(j)
	return jsonify(items)	

if __name__ == "__main__":
    app.debug = True
    app.run()