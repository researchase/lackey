class FindFailed(Exception):
	def __init__(self,*args,**kwargs):
		Exception.__init__(self,*args,**kwargs)