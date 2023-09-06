a='Hello'
b=a+'There'
c=a+' '+'There'
print(b)
print(c)
if 'o' in a:
    print('found it')

z=a.lower()
print(z)
print(a)

pos=a.find('o')
print(pos)

greet='Hello There'
rep=greet.replace('There', 'adam')
print(rep)

greet=' hello bob '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

line='Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
spos=data.find(' ',atpos)
print(spos)
host=data[atpos+1:spos]
print(host)
