from dao.py import TaskDao

class Model:

	def find_by_id(task_id):
		dao = TaskDao()
		task = dao.get_task_by_id(task_id)
		model = Model(task) if model else None

		return model

	def find_by_params(kwargs):

	def create_task(task):

	def delete_task(task_id)