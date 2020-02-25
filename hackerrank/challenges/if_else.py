n = int(input(""))
if n % 2 == 1:
    print("Weird")
elif 1 < n < 6:
    print("Not Weird")
elif 5 < n < 21:
    print("Weird")
elif n > 20:
    print("Not Weird")
else:
    print("Invalid input")