from pymongo import MongoClient

TODOS = [ 
	{
	'id': 1,
	'todo': 'Achieve world peace',
	'completed': False
	},
	{
	'id': 2,
	'todo': 'Cure cancer',
	'completed': False
	},
	{
	'id': 3,
	'todo': 'Become a billionaire',
	'completed': False
	},
	{
	'id': 4,
	'todo': 'Become a Pokemon master',
	'completed': True
	},
	{
	'id': 5,
	'todo': 'Get a girlfriend',
	'completed': False
	},
]

client = MongoClient()
db = client.test_database

TODOS = db.todos




