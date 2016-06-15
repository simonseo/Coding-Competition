n = int(input())
l1 = list(map(int, input())).sort()
l2 = list(map(int, input())).sort()
l3 = list(map(int, input())).sort()

index = n-1
max = n-1
min = 0
while(True):
	if index == 0:
		return l1[index]
	else:
		if l1[index] < l2[index] and l1[index-1] == l2[index-1]:
			break
		elif l1[index] == l2[index]:
			min = index
			index = (min + max)/2
		elif l1[index] < l2[index]:
			max = index
			index = (min + max)/2
