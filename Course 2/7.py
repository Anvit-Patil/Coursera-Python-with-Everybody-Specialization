fhand=open('mbox.txt')
#inp=fhand.read()
#print(len(inp))
#print(inp[:20])

count=0
for line in fhand:
    if count<10:
        if line.startswith('From:'):
            count=count+1
            print(line)
print('-----------------------------------------')
fhand=open('mbox.txt')
count=0
for line in fhand:
    if count<10:
        if line.startswith('From:'):
            count=count+1
            line=line.rstrip()
            print(line)
print('-----------------------------------------')
fhand=open('mbox.txt')
count=0
for line in fhand:
    if count<10:
        if not line.startswith('From:'):
            continue
        count=count+1
        line=line.rstrip()
        print(line)
print('-----------------------------------------')

fname=input('Enter the file name:')
try:
    fhand=open(fname)
except:
    print('wrong file')
    quit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('there were', count, 'subject lines in',fname)
