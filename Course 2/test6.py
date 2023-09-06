text = "X-DSPAM-Confidence:    0.8475";
atpos=text.find('0')
host=text[atpos:]
host1=float(host)
print(host1)
