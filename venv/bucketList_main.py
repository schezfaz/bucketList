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
	goals = []
	goal = bucketList.find()
	for j in goal:
		j.pop('_id')
		goals.append(j)
	return jsonify(goals)	

@app.route('/addGoal/<new_goal>', methods=['POST']) #adding new item to bucketlist
def add_item(new_goal):
	bucketList = mongo.db.bucketList
	goal_new = {'name' : new_goal}
	if bucketList.find({'name' : new_goal}).count() > 0:
		return "Item Already Exists!"
	else:
		bucketList.insert(goal_new)
		return "Added item successfully"

@app.route('/delete/<goal_name>', methods=['GET']) #function to delete one item on bucketlist
def delete_item(goal_name):
	bucketList = mongo.db.bucketList
	bucketList.remove({'name': goal_name})
	return "Item deleted successfully!"


if __name__ == "__main__":
    app.debug = True
    app.run()