'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143

'''

def is_prime(num):
	for j in range(2,x-1):
		if x % j == 0:
			return False
	return True

i = raw_input("\nInput a large number >> ")

j = int(i)

n = int((j) / 2 + 1)

print "Here is half of what your input: %d" % n

print "Here are some factors of %d:" % j

for x in range(1, n):
	if j % x == 0:
		print x
		if is_prime(x) == True:
			print "This is your largest prime factor: %d" % x
			break