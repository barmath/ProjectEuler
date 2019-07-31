
def fib(n):

	fibonacci = []
	a,b = 1,2
	limit = 4000000

	while a< n:
		if a%2 == 0 and a<limit:
			fibonacci.append(a)
		a,b = b, a+b
		

	return sum(fibonacci)

if __name__ == '__main__':
	print(fib(5000000000))
