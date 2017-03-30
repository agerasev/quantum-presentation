#!/usr/bin/python3

import math

n = 21

for i in range(2, n - 1):
	p = 1
	for j in range(1, 10):
		p = (p*i) % n
		if p == 1:
			print("%d^%d == %d" % (i, j, p))
			if (j % 2) != 0:
				print("\t%d is odd, fallback" % j)
			else:
				m = i**(j//2)
				print("\t%d^(%d/2) == %d" % (i, j, m))
				if (m % n) == n - 1:
					print("\t%d %% %d == %d, fallback" % (m, n, n - 1))
				else:
					gs = [math.gcd(m + 1, n), math.gcd(m - 1, n)]
					print("\tgcd(%d + 1, %d) == %d, done" % (m, n, gs[0]))
					print("\tgcd(%d - 1, %d) == %d, done" % (m, n, gs[1]))