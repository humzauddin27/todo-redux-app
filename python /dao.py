from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.test_database

TODOS = db.todos
num_todos = 5

class TaskDao:

	def get_task_by_id(self, task_id):
		result = TODOS.find_one({"id": int(task_id)})
		return result

	def get_all_tasks(self):
		return TODOS.find()

	def create_task(self, task):
		new_task={
			"id": (num_todos+1),
			"todo": task,
			"completed": False
		}
		TODOS.insert(new_task)
		return new_task


	#def update_task(self, task_id, task):

	#def delete_task(self, task_id):