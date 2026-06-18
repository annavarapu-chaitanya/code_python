colors = ["navyblue", "black", "violat", "wine", "orange"]

color1 = input("Enter first color: ")
color2 = input("Enter second color: ")

if color1 in colors and color2 in colors:
    print(f"Mixing {color1} and {color2}")
else:
    print("One or both colors are not available")
