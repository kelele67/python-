while True:
	i = raw_input()
	n, m = map(int, i.split(' '))
	A = list(raw_input().split())
	B = list(raw_input().split())
	C = list(set(A+B))
	C = map(eval, C)
	C.sort()
	for c in C:
		print c