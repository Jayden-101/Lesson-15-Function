def calculate_circumference(radius):
    pi = 3.14159
    return 2*pi*radius

def main():
    radius = float(input("Enter the radius of the circle"))
    if radius < 0:
        print("Radius cannot be negative")
    else:
        circumference = calculate_circumference(radius)
        print(f"The circumference of the circle is: {circumference:.2f}")

main()