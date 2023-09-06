def computepay(h,r):
    p1=h*r
    p2=((h-40)*(1.5*r))+420
    if h<=40:
        return p1
    else:
        return p2


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hr = float(hrs)
rt= float(rate)
p = computepay(hr,rt)
print("Pay",p)
