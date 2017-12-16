def debug(iterable):
	if(type(iterable)==type(list('a'))):
		print('aaa')
	else:
		print(type(iterable))


z = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
debug(z)
