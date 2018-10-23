user_input = input("Enter Filename: ")

count = 0
number_of_lines = 0

fhand = open(user_input)
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):        
        line = line.replace("X-DSPAM-Confidence:", "")
        #print(line)
        number_of_lines = number_of_lines + 1
        count = count + float(line)

rezultats = count / number_of_lines
print("Average spam confidence:", rezultats)
        

