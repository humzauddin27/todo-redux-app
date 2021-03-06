from dao import TaskDao

class Model:

	def __init__(self, collection=[]):
		if (collection == None):
			return
		self.id = collection['id']
		self.task =	collection['todo']
		self.completed = collection['completed']

	def find_by_id(task_id):
		dao = TaskDao()
		task = dao.get_task_by_id(task_id)
		model = Model(task).__dict__

		return model

	def get_all_tasks():
		dao = TaskDao()

		listTasks = dao.get_all_tasks()
		new_list = []
		for i in listTasks:
			new_list.append(Model(i).__dict__)


		return new_list


#	def find_by_params(kwargs):
#		dao = TaskDao()
#		task_collection = dao.get_task_by_params(kwargs)

#		task_models = [task_collection.pop(0)] + [Model(task).__dict__ for task in task_collection]
#		return task_models

	@staticmethod
	def create_task(task):
		dao = TaskDao()
		new_task = dao.create_task(task)
		task_model = Model(new_task).__dict__
		return task_model

	def delete_task(task_id):
		dao = TaskDao()
		response = dao.delete_task(task_id)

		if response:
			response = {'message': 'task was deleted successfully'}

		return response

