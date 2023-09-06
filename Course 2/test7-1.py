fname = input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1
print("Done")
