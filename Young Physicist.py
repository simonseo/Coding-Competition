n = int(input())
vectors = []
x = 0
y = 0
z = 0
for i in range(n):
	vectors += (list(map(int, input().split())))
for i in range(len(vectors)):
	if i % 3 == 0:
		x += vectors[i]
	elif i % 3 == 1:
		y += vectors[i]
	elif i % 3 == 2:
		z += vectors[i]
if (x == 0) and (y == 0) and (z == 0):
	print('YES')
else:
	print('NO')
