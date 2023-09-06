name=input('Enter file: ')
if len(name) < 1 : name = "mbox-short.txt"
handle=open(name)
nwords=list()
fwords=list()
time=list()
owords=list()
counts=dict()
for line in handle:
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
        nwords=words[5]
        time=nwords.split()
        owords=time[0]
        owords=owords.split(':')
        fwords=owords[0]
        fwords=fwords.split()
        for word in fwords:
            counts[word]=counts.get(word,0)+1     #histogram is created

for word,count in sorted(counts.items()):
    bigword=word
    bigcount=count
    print(bigword,bigcount)
