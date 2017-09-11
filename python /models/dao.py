from pymongo import MongoClient

TODOS = [ 
	{
	'id': 1,
	'todo': 'Achieve world peace',
	'completed': false
	},
	{
	'id': 2,
	'todo': 'Cure cancer',
	'completed': false
	},
	{
	'id': 3,
	'todo': 'Become a billionaire',
	'completed': false
	},
	{
	'id': 4,
	'todo': 'Become a Pokemon master',
	'completed': true
	},
	{
	'id': 5,
	'todo': 'Get a girlfriend',
	'completed': false
	},
]

client = MongoClient()
db = client.test_database

TODOS = db.todos

class TaskDao:

	def get_connection(self):

	def get_task_by_id(self, task_id):

	def get_task_by_params(self, kwargs):

	def create_task(self, task):

	def update_user(self, task_id, task):

	def delete_user(self, task_id):





