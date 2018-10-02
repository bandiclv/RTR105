def pirmais_uzd():

    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hours <= 40:
        pay = hours * rate
    
        print(pay)

    if hours > 40:
        extra_rate = 1.5 * rate
        extra_hours = hours - 40

        hrs = hours - extra_hours

        pay = (hrs * rate) + (extra_rate * extra_hours)
    
        print(pay)

pirmais_uzd()


def otrais_uzd():

    score = float(input("Enter Score: "))

    if score<0 or score>1:
        print("Error!")
        return;
        
    elif score >= 0.9:
        print("A")
        return;
    elif score >= 0.8:
        print("B")
        return;
    elif score >= 0.7:
        print("C")
        return;
    elif score >= 0.6:
        print("D")
        return;
    elif score < 0.6:
        print("F")
        return;


otrais_uzd()        
