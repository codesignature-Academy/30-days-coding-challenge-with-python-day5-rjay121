while True:

    number = int(input("Enter a number: "))
    if number > 0:
        print(f"{number} is Positive")
    elif number < 0:
        print(f"{number} is Negative")
    else:
        print("Zero")
    
    exit = input("do you want to exit? (type q to exit) or (type c to continue) ")
    if exit == "q":
        print("Goodbye")
        break
    elif exit == "c":
        print("Let's continue")
        continue
   

