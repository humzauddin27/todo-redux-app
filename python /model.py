from dao import TaskDao

class Model:

	def __init__(self, collection=[]):
		self.id = collection['id']
		self.task =	collection['task']
		self.completed = collection['completed']

	def find_by_id(task_id):
		dao = TaskDao()
		task = dao.get_task_by_id(task_id)
		model = Model(task) if model else None

		return model

#	def find_by_params(kwargs):
#		dao = TaskDao()
#		task_collection = dao.get_task_by_params(kwargs)

#		task_models = [task_collection.pop(0)] + [Model(task).__dict__ for task in task_collection]
#		return task_models

	def create_task(task):

		dao = TaskDao()
		new_task = dao.create_task(task)
		task_model = Model(new_task) if new_task else None

		return task_model

	def delete_task(task_id):
		dao = TaskDao()
		response = dao.delete_task(task_id)

		if response:
			response = {'message': 'task was deleted successfully'}

		return response

	def get_all_tasks():
		dao = TaskDao()

		listTasks = dao.get_all_tasks()
		for i in listTasks:
			i = Model(i) if i else None
