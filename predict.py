import sys

fp = open("review.adj","w")

def window(iterable, size):
	i = iter(iterable)
	win = []
	for e in range(0, size):
		win.append(next(i))
	yield win
	
	for e in i:
		win = win[1:] + [e]
		yield win



for line in sys.stdin:
	a = line.split()
	bedsize = len(a)
	winsize = 5
	b = window(a,winsize)
	for i in range(0,bedsize-winsize+1):
		for x in next(b):
			fp.write(x+',')
			
		fp.write('\r\n')
	
	
	if 1 :
		break

fp.close()



