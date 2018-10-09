def computepay(hours, rate):


    if hours <= 40:
        pay = hours * rate

        print(pay)

    if hours > 40:
        extra_hours = hours - 40
        extra_rate = 1.5 * rate

        hrs = hours - extra_hours
        
        pay = (hrs * rate) + (extra_rate * extra_hours)

        print(pay)
        return pay


h = float(input('Enter Hours: '))
r = float(input('Enter Rate: '))

computepay(h,r)

