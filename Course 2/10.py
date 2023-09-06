#tuples
'''
x=('glenn','Sally','joseph')
print(x[2])
y=(1,2,3,9)
print(y)
print(max(y))
''' '''
z=(2,3,4)
z[2]=1          #traceback since non mutable
'''
'''
(x,y)=(4,"fred")
print(y)

if (0,1,2)<(5,1,2):
    print("true1")
if (0,1,200)<(0,3,4):
    print("true2")
if ('Jones','Sally')<('Jones','Sam'):
    print("true3")
if ('jones','sally')>('adams','sam'):
    print("true4")
'''

d={'a':10,'b':1,'c':22}
#print(d.items())
#print(sorted(d.items()))
for k,v in sorted(d.items()):      #sort in key order
    print(k,v)

c={'a':10,'b':1,'c':22}         #sort key wisse
tmp=list()
for k,v in c.items():
    tmp.append((v,k))           #make a v,k tuple
print(tmp)
tmp=sorted(tmp,reverse=True)        #desending order
print(tmp)
