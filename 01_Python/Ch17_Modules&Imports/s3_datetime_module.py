import datetime

print(datetime.datetime.now())  # module.class.method
print(datetime.datetime.today())
print(datetime.datetime.utcnow())

# time
my_time = datetime.time(13, 44, 1, 20)  # (h, ,m, s, ms)
print(my_time)  # 13:44:01.000020
print(my_time.hour)  # 13
print(my_time.minute)  # 44

# date
x = datetime.date.today()
print(x)  # 2021-06-23
print(x.year)
print(x.month)
print(x.day)
print(x.ctime())    # Wed Jun 23 00:00:00 2021

