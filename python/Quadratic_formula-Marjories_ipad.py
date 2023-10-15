import math

from character_type_class import int_float
from fraction_simplifier_class import fraction, simplifier
from squareroot_class import Factor, Squareroot

a = int(input("Enter a: "))#float
b = int(input("Enter b: "))#float
c = int(input("Enter c: "))#float
denominator = 2 * a
InSqrt = (b**2) - (4 * a * c)

if InSqrt < 0:
    InSqrt = abs(InSqrt)
    print("NO SOLUTION")

print(f"\n{-b}±√{b}² {-4}({a})({c})\n    {2}({a})") #formula


char_type = (int_float(math.sqrt(InSqrt)).int_float()) #checks if number has perfect sqrt
factors = Factor(InSqrt).char_type_sqrt()
Sqrt_ans = Squareroot(factors, InSqrt).answer()
if char_type == "float":
    print((f"\n {-b}±√{b**2} + {-4 * a * c}\n    {denominator}"))
    print((f"\n  {-b}±√{InSqrt}\n    {denominator}"))
    if Sqrt_ans == None:
      print(f"\n{-b} + √{factors[0]}  |  {-b} - √{factors[0]}\n    {denominator}    |     {denominator}")
    else:
      print(f"b\n{-b} + {Sqrt_ans[5:]}  |  {-b} - {Sqrt_ans[5:]}\n    {denominator}    |     {denominator}")
      #print(f"\n    {Sqrt_ans[5:]}\n     {denominator}")

else:
    print((f"\n {-b}±√{InSqrt}\n    {denominator}"))
    print(f"\n{-b} + {int(math.sqrt(int(Sqrt_ans[5:])))}  |  {-b} - {int(math.sqrt(int(Sqrt_ans[5:])))}\n    {denominator}    |     {denominator}")

    positive = (f"{-b + int(math.sqrt(int(Sqrt_ans[5:])))}/{denominator}")
    negative = (f"{-b - int(math.sqrt(int(Sqrt_ans[5:])))}/{denominator}")

    pos_ans = fraction(positive).nums()
    pos_fraction = simplifier(pos_ans).simplify()

    neg_ans = fraction(negative).nums()
    neg_fraction = simplifier(neg_ans).simplify()
    print(f"\n{positive} -> x = {pos_fraction}")
    print(f"\n{negative} -> x = {neg_fraction}")
