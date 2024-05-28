import math
from character_type_class import int_float
from squareroot_class import Factor
from squareroot_class import Squareroot
from fraction_simplifier_class import fraction
from fraction_simplifier_class import simplifier

a = int(input("Enter a: "))#float
b = int(input("Enter b: "))#float
c = int(input("Enter c: "))#float



denominator = 2 * a
InSqrt = (b**2) - (4 * a * c)

if InSqrt < 0:
  InSqrt = InSqrt * -1

formula = (f"\n{-b}±√{b}² {-4} * {a} * {c}\n    {2} * {a}")
print(formula)


char_type = (int_float(math.sqrt(InSqrt)).int_float()) #checks if number has perfect sqrt

if char_type == "float":
  factors = Factor(InSqrt).char_type_sqrt()
  Sqrt_ans = Squareroot(factors, InSqrt).answer()


  
  if (b**2 + (-4 * a * c) < 0):
    print('\nnote: you can not square root a negative number')

  if((-4 * a * c) < 0):
    print((f"\n{-b}±√{b**2} {-4 * a * c}\n    {denominator}"))
  else:
    print((f"\n {-b}±√{b**2} + {-4 * a * c}\n\t{denominator}"))
    print((f"\n  {-b}±√{InSqrt}\n    {denominator}"))

  if Sqrt_ans == None:
    print(f"\n{-b} + √{factors[0]}\t|\t{-b} - √{factors[0]}\n    {denominator}\t\t|\t    {denominator}")
  else:
    print(f"\n{-b} + {Sqrt_ans[5:]}\t|\t{-b} - {Sqrt_ans[5:]}\n    {denominator}\t\t|\t    {denominator}")
  
else:
  print((f"\n {-b}±√{b**2}{-4 * a * c}\n    {denominator}"))
  print((f"\n  {-b}±√{InSqrt}\n    {denominator}"))


  print(f"\n{-b} + {int(math.sqrt(InSqrt))}\t  |\t{-b} - {int(math.sqrt(InSqrt))}\n   {denominator}\t  |\t   {denominator}")
 

  positive = (f"{-b + int(math.sqrt(InSqrt))}/{denominator}")
  negative = (f"{-b - int(math.sqrt(InSqrt))}/{denominator}")

  pos_ans = fraction(positive).nums() 
  pos_fraction = simplifier(pos_ans).simplify()
  
  neg_ans = fraction(negative).nums()
  neg_fraction = simplifier(neg_ans).simplify()
  
  
  print(f"\n{positive}\n ↓ \n{pos_fraction}")
  print(f"\n{negative}\n ↓ \n{neg_fraction}")

  print(f"\nAnswers:\n{pos_fraction}  ,  {neg_fraction}\n")
