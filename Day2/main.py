from shapes import circle, rectangle

# Circle calculations
r=int(input('Enter the radius of circle'))
print(f"Circle Area: {circle.area(r):.2f}")
print(f"Circle Perimeter: {circle.perimeter(r):.2f}")

# Rectangle calculations
l=int(input('Enter the length'))
w=int(input('enter the width'))
print(f"Rectangle Area: {rectangle.area(l, w)}")
print(f"Rectangle Perimeter: {rectangle.perimeter(l, w)}")
