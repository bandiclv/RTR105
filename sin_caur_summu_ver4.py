from math import sin

x = float(input("Lietotaj, ludzu, ievadiet argumentu (x): "))

y = sin(x)
print ("sin(%.2f) = %.2f"%(x, y))

k = 0
a = (-1)**0*x**1/(1)
S = a
print ("a0 = %6.2f S0 = %6.2f"%(a,S))

k = 1
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
print ("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

k = 2
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
print ("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

k = 3
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
print ("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))