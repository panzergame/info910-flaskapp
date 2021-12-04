from .db import db


class Message(db.Model):
	__tablename__ = 'message'

	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(1024))

	def __init__(self, content):
		self.content = content
