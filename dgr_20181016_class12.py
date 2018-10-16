text = "X-DSPAM-Confidence:    0.8475";

x = text.find(" ")
print(x)

y = text.find("5", x)
print(y)

txt = text[x:y+1]
print(float(txt))






