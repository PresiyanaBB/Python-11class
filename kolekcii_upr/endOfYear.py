import datetime

print('input must be dd.mm.yyyy')
n = []
n = str(input())
dd = int(n[:2])
mm = int(n[3:5])
yyyy = int(n[6:10])
date = datetime.date(yyyy,mm,dd)
future = datetime.date(yyyy,12,31)
print (f'days left: {(future - date).days}')
