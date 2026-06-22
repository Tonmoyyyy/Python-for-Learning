n = int(input("Enter a number: "))

if n % 3 == 0 and n % 4 == 0 and n % 5 == 0:
    print("not possible")

elif n % 3 == 0 and n % 4 == 0:
    print("future")

elif n % 3 == 0:
    print("Argentina")

elif n % 4 == 0:
    print("Germany")

elif n % 5 == 0:
    print("Brazil")

else:
    print("None")