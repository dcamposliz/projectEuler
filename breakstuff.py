grow1 = 1

for x in range(0,100):
	grow1 = grow1 + grow1
	print grow1

# the ABOVE actually prints exponential growth :P

# we need to refine what we're trying to do !!

#-----------------------------#

a = 1
b = 1


for x in xrange(1,10):
	c = a + b
	a = b
	b = c
	print c
