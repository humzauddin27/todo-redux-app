from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.test_database

TODOS = db.todos

class TaskDao:

	def get_task_by_id(self, task_id):
		return TODOS.find({"id":task_id})

	def create_task(self, task_id, task):
		return TODOS.insert({
			"id": task_id,
			"task": task,
			"completed": false
			})

	def get_all_tasks(self):
		return TODOS.find()

	#def update_task(self, task_id, task):

	#def delete_task(self, task_id):