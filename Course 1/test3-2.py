hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r= float(rate)
except:
    print('Error,enter numeric input.')
    quit()

pay=h*r
p=((h-40)*(1.5*r))+420
if h<=40:
    print(pay)
else:
    print(p)
