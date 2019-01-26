# this program will be a calculator for various shapes that a user can input.
print
"Calculator engaging......"
option = input("Enter C for circle or T for triangle ")
if option == "C":
    radius = float(input("What is the radius? "))
    area = 3.14159 * radius ** 2
    print(str(area))
elif option == "T":
    base = float(input("What is the base? "))
    height = float(input("What is the height? "))
    area2 = .5 * (base * height)
    print(str(area2))
else:
    print("invalid shape")
