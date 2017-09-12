from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from model import Model

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('todo')

class Todo(Resource):
	def get(self, id):
		task_model = Model.find_by_id(id)
		print(task_model)
		return task_model

	#def post(self):
		#TODOS[]

	##delete(self) 

class TodoList(Resource):
	def get(self):
		task_model = Model.get_all_tasks()
		the_list = []
		for i in task_model:
			the_list.append(i)

		return the_list

	#def post(self):


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<id>')

if __name__ == '__main__':
    app.run(debug=True)
