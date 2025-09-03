
class Manager:
	def __init__ (self, db):
		self.db = db

	def get_user(self, user):
		pass

	def craete_Users_table(self):
		self.db.create_table("Users")