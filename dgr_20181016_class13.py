# Use the file name mbox-short.txt as the file name
values = []
fname = raw_input("Enter file name: ")
with open(fname) as fh:
    for line in fh.read().split('\n'):
        if line.startswith('X-DSPAM-Confidence:'):
            values.append(line.replace('X-DSPAM-Confidence: ', '')) 

values = [float(i) for i in values]
print 'Average spam confidence: %f' % float( sum(values) / len(values))
