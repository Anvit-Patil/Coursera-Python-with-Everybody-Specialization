name=input('Enter file: ')
if len(name) < 1 : name = "mbox-short.txt"
handle=open(name)
nwords=list()
counts=dict()
for line in handle:
    if line.startswith('From:'):
        words=line.split()
        print(words)
'''
        nwords=words[5]
        nwords=nwords.split()
        #print(nwords)
        for word in nwords:
            counts[word]=counts.get(word,0)+1     #histogram is created

bigcount=None
bigword=None
for word,count in counts.items():
    bigword=word
    bigcount=count
    print(bigword,bigcount)
'''
