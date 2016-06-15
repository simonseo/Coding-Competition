small = ['q','r','b','n','p']
BIG = ['Q','R','B','N','P']
weight = [9,5,3,3,1]
inList = []
smallSum = 0
bigSum = 0

for i in range(8):
	inString = input().strip()
	for char in inString:
		if char in small:
			smallSum += weight[small.index(char)]
		elif char in BIG:
			bigSum += weight[BIG.index(char)]
if bigSum > smallSum:
	print('White')
elif bigSum < smallSum:
	print('Black')
elif bigSum == smallSum:
	print('Draw')