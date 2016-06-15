hh, mm = map(int, input().split(':'))
a = int(input())
hh = int((hh + ((mm + a) / 60)) % 24)
mm = (mm + a) % 60
print('{0:02d}:{1:02d}'.format(hh,mm))