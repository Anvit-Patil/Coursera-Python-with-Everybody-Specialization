"""
abc='With three words  and   spaces'
print(abc)
stuff=abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)

line='first;second;third'
thing=line.split()
print(thing)
print(len(thing))
thing=line.split(';')
print(thing)
print(len(thing))
"""
line='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words=line.split()
print(words)
email=words[1]
pieces=email.split('@')
print(pieces)
