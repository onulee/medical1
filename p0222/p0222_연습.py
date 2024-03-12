import datetime 
now = datetime.datetime.now()
year = now.year

h = now.hour
if h < 12:
    print("현재는 {}시로 오전입니다.".format(h))
else: 
    print('현재는 {}시로 오후입니다.'.format(h))