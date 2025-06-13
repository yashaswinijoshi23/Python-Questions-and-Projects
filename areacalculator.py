import math #it provides the value of π (pi) with high precision
print("----------------Area calculator---------------")

def area_of_rectangle():
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))
    area = length * breadth
    print(f"The area of rectangle is {area} units")

def area_of_square():
    side = int(input("Enter the size of the side: "))
    area = side * side
    print(f"The area of square is {area} units")

def area_of_triangle():
    breadth = int(input("Enter the breadth: "))
    height = int(input("Enter the height: "))
    area = (breadth * height) * 0.5
    print(f"The area of triangle is {area} units")

def area_of_circle():
    radius = int(input("Enter the radius: "))
    area = (radius ** 2) * math.pi
    print(f"The area of circle is {area} units")

while True:
    choice = input("Who's area do you want me to calculate?\n Square\n Triangle\n Circle\n Rectangle\n")

    if choice == "Square":
        area_of_square()
    elif choice == "Triangle":
        area_of_triangle()
    elif choice == "Circle":
        area_of_circle()
    elif choice == "Rectangle":
        area_of_rectangle()
    elif choice == "Exit":
        print("Exiting the calculator. See you again!")
        break
    else:
        print("Invalid choice. Please try again")