class booking:
	def __init__(self, usr, rum, startTime, endTime, amountReq, reason=""):
		self.usr=usr
		self.rum=rum
		self.startTime=startTime
		self.endTime=endTime
		self.amountReq=amountReq
		self.amountPaid=0
		self.status="init"
		self.reason=reason
	def check(self, usr, checkOutTime):
	def refund(self):
	def getStatus(self):
