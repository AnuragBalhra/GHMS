class room:
	def __init__(self, cost):
		self.cost=cost
		self.status='Available'

	def checkStatus(self):
		return self.status

	def changeStatus(self):
		if(self.status=='Available'):
			self.status='Not Available'
		else:
			self.status=='Available'	