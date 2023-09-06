f='Banana'
l=f[1]
print(l)
x=3
w=f[x-1]
print(w)
print(len(f))

i=0
while i<len(f):
    x=f[i]
    print(i,x)
    i=i+1

for y in f:
    print(y)

count=0
for z in f:
    if z=='a':
        count=count+1
print(count)

s='Monty Python'
print(s[0:4])   #upto but not including 4
print(s[6:7])
print(s[6:20])
