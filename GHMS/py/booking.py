class booking:
	def __init__(self, usr, rum=None, startTime, endTime, amountReq, reason=""):
		self.usr=usr
		self.rum=rum
		self.startTime=startTime
		self.endTime=endTime
		self.amountReq=amountReq
		self.amountPaid=0
		self.status="init"
		self.reason=reason
	def check(self, usr, checkOutTime):
		return (self.usr==usr and self.endTime> checkOutTime)
		# pay attention that if endTime<= checkOutTime then it will return false

	def refund(self):
		refundAmount=self.amountPaid
		# External refund Process
		return refundAmount

	def getStatus(self):
		return self.status
