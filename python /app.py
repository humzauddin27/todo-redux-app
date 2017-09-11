from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

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
	'completed': False
	},
	{
	'id': 5,
	'todo': 'Get a girlfriend',
	'completed': False
	},
]

class Todo(Resource):
	def get(self, id):
		return TODOS[int(id) - 1]
	#def post(self):
		#TODOS[]

	##delete

class TodoList(Resource):
	def get(self):
		return TODOS
	##put


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<id>')

if __name__ == '__main__':
    app.run(debug=True)
