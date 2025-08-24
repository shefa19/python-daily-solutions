import datetime

a = datetime.datetime.now()
print(a)


b = datetime.datetime.now()
print(b.year)
print(b.strftime("%A"))


c = datetime.datetime(2025, 5, 17)
print(c)


d = datetime.datetime(2025, 8,23)
print(d.strftime("%B"))
