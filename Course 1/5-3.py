print('count')
count=0
print('Before',count)
for t in [9,41,12,3,74,15]:
    count=count+1
    print(count,t)
print('After',count)
print('------------------------')
print('sum')
sum=0
print('Before',count)
for t in [9,41,12,3,74,15]:
    sum=sum+t
    print(sum,t)
print('After',sum)
print('------------------------')
print('avg')
count=0
sum=0
print('Before',count,sum)
for t in [9,41,12,3,74,15]:
    count=count+1
    sum=sum+t
    print(sum,count,t)
print('After',sum,count,"avg",sum/count)
print('------------------------')
print('larger than')
for t in [9,41,12,3,74,15]:
    if t>20:
        print ('large number',t)
print('------------------------')
print('Find 3')
found=False
print('Before',found)
for t in [9,41,12,3,74,15]:
    if t==3:
        found=True
        break
    print(found,t)
print('After',found,t)
print('------------------------')
print('smallest')
smallest=None
for t in [9,41,12,3,74,15]:
    if smallest is None:
        smallest=t
    elif t<smallest:
        smallest=t
    print(smallest,t)
print('------------------------')
