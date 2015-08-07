m = raw_input("Give me a large number: ")
n = int(m)
i = 2

while i * i < n:
	while n % i == 0:
		n = n / i
	i = i + 1
print n