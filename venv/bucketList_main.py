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

@app.route('/addItem/<new_item>', methods=['POST']) #adding new item to bucketlist
def add_item(new_item):
	bucketList = mongo.db.bucketList
	item_new = {'name' : new_item}
	if bucketList.find({'name' : new_item}).count() > 0:
		return "Item Already Exists!"
	else:
		bucketList.insert(item_new)
		return "Added item successfully"

@app.route('/delete/<item_name>', methods=['GET']) #function to delete one item on bucketlist
def delete_item(item_name):
	bucketList = mongo.db.bucketList
	bucketList.remove({'name': item_name})
	return "Item deleted successfully!"


if __name__ == "__main__":
    app.debug = True
    app.run()