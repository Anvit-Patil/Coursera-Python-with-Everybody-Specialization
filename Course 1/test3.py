hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r= float(rate)
pay=h*r
p=((h-40)*(1.5*r))+420
if h<=40:
    print(pay)
else:
    print(p)
