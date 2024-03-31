def delay(arg):
	print('delayed')
	def g():
		return arg
	return g