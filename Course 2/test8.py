fname = input("Enter file name: ")
fh = open(fname)
lst = list()
x=list()
for line in fh:
    x=x+line.split()
for i in x:
    if not i in lst:
        lst.append(i)
lst.sort()
print(lst)
