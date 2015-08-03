'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143

'''

i = raw_input("")
n = int(i)
for x in range(2, n):
	if n % x == 0:
		if is_prime(x) == True:
			print x