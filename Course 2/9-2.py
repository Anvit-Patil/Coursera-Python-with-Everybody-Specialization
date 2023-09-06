"""
counts=dict()
print('enter line:')
line=input('')
words=line.split()
print('Words',words)
print('Countting...')
for word in words:
    counts[word]=counts.get(word,0)+1
print('counts',counts)
"""
'''
counts={'chuck':1,'fred':42,'jan':100}
for key in counts:
    print(key,counts[key])
'''
'''
jjj={'chuck':1,'fred':42,'jan':100}
print(list(jjj))            #keys
print(jjj.keys())
print(jjj.values())
print(jjj.items())

for k,v in jjj.items():
    print(k,v)
'''
