#from flask import Flask, jsonify
#from flask_restful import Resource, Api, request

#app = Flask(__name__)
#api = Api(app)

tasks = [
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
	'completed': False
	},
	{
	'id': 5,
	'todo': 'Get a girlfriend',
	'completed': False
	},
]

def get(id):
	return tasks[0]

print(get(0))