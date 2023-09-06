fname=input('Enter the file name:')
fhand=open(fname)
count=0
u=0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
            line=line.rstrip()
            t=line[20:]
            r=float(t)
            u=u+r
            count=count+1
print('Average spam confidence:', u/count)
