def Pirmais_Uzd():
    Hours = 45
    Rate = 10

    Pay = 40 * 10 + 5 * 15

    Pay_as_float = float(Pay)

    print(Pay_as_float)

Pirmais_Uzd()

def Otrais_Uzd():
    print("Rate must be 2.75")
    rate = float(input("Enter Rate: "))

    #hrs = 35.0
    print("Hours must be 35")
    hrs = float(input("Enter Hours: "))

    pay = rate*hrs

    print("Pay: ",pay)

Otrais_Uzd()
