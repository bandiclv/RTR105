numbers_entered = []
while True:
    user_input = raw_input("Enter a number: ")
    if user_input == "done":
        break
    try:
        numbers_entered.append(int(user_input))
    except ValueError:
        print("Invalid input")

if numbers_entered:
    print("Maximum is", (max(numbers_entered)))
    print("Minimum is", (min(numbers_entered)))
    
