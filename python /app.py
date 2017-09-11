from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
 
parser = reqparse.RequestParser()
parser.add_argument('todo')

class Todo(Resource):
	def get(self, id):
		return TODOS[int(id) - 1]
	#def post(self):
		#TODOS[]

	##delete(self) 

class TodoList(Resource):
	def get(self):
		return TODOS
	def post(self):
		args = parser.parse_args()
		newID = len(TODOS) + 1
		newItem = {
			'id': newID,
			'todo': args['todo'],
			'completed': False
		}
		TODOS.append(newItem)
		return newItem


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<id>')

if __name__ == '__main__':
    app.run(debug=True)
