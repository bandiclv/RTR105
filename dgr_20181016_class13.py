values = []
filename = input("Enter file name: ")
with open(filename) as fh:
    for line in fh.read().split('\n'):
        if line.startswith('X-DSPAM-Confidence:'):
            values.append(line.replace('X-DSPAM-Confidence: ', '')) 

values = [float(i) for i in values]
print(values)
print ("Average spam confidence: %.12f" % float( sum(values) / len(values)))
