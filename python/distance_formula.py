import math

x1, y1 = input("Enter first coordinate: ").split()
x2, y2 = input("Enter second coordinate: ").split()

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

print(f"\nd = √({x2} - {x1})² + ({y2} - {y1})²")
print(f" d = √{pow(x2 - x1, 2)} + {pow(y2 - y1, 2)}")
print(f"   d = √{pow(x2 - x1, 2) + pow(y2 - y1, 2)}")

from squareroot_class import Factor
from squareroot_class import Squareroot

factors = Factor(pow(x2 - x1, 2) + pow(y2 - y1, 2)).char_type_sqrt()

Sqrt = Squareroot(factors, pow(x2 - x1, 2) + pow(y2 - y1, 2)).answer()
