from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from model import Model

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('todo')

class Todo(Resource):
	def get(self, task_id):
		task_model = Model.find_by_id(task_id)
		data = task_model.jsonify(task_model.__dict__)
		return data

	#def post(self):
		#TODOS[]

	##delete(self) 

class TodoList(Resource):
	def get(self):
		task_model = Model.get_all_tasks()
		the_list = task_model.jsonify(task_model.__dict__)
		return the_list

	#def post(self):


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<id>')

if __name__ == '__main__':
    app.run(debug=True)
