from math import sin

x = float(input("Lietotaj, ludzu, ievadiet argumentu (x): "))

y = sin(x)
print ("sin(%.2f) = %.2f"%(x, y))

a = (-1)**0*x**1/(1)
S = a
print ("a0 = %.2f S0 = %.2f"%(a, S))

a = (-1)*x*x/(2*3)
S = S + a
print ("a1 = %.2f S1 = %.2f"%(a, S))

a = (-1)*x*x/(4*5)
S = S + a
print ("a2 = %.2f S2 = %.2f"%(a, S))

a = (-1)*x*x/(6*7)
S = S + a
print ("a3 = %.2f S3 = %.2f"%(a, S))
