
import math
##	a = (float(input()))
for a in range(1000):
	if a == 2:
		
		print(1)
		print()
	else:
		b = (math.sqrt(1+8*a)/2)
		if b - int(b) == 0.5:
			
			print (int(b))
			print()
			
		else:
			sum = int(b-0.5)*int(b+0.5)/2
			print (int(a % sum))
			