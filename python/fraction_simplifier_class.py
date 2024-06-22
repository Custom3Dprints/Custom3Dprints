from greatest_common_factor import GreatestCommonFactor

class fraction: #input string ex: "6/2"
    def __init__(self, fraction):
        self.fraction = fraction

    def nums(self): #exput (numerator, denominator)
        numerator = ""
        for n in range(len(self.fraction)):
            if self.fraction[n] != "/":
                numerator += self.fraction[n]

            elif self.fraction[n] == "/":
                denominator = int(self.fraction[n+1:])
                break
        #numerator = int(numerator)
        return (int(numerator), int(denominator))

class simplifier: #input needed tuple from fraction(nums).simplify() ex: (6,2)
    def __init__(self, fraction):
        self.fraction = fraction
    
    def simplify(self):
        numerator = self.fraction[0]
        denominator = self.fraction[1]
        if numerator == 0:
            return 0
        elif numerator < 0: #if numerator is negative
            numerator = abs(numerator) #absolute value of number
            gcf = GreatestCommonFactor(numerator, denominator).gcf()
            
            if (denominator/gcf) == 1:
                return (f"-{int(numerator/gcf)}")
            else:
                return (f"-{int(numerator/gcf)}/{int(denominator/gcf)}")

        elif denominator < 0:
            denominator = denominator*-1
            numerator_F = [num for num in range(1, numerator + 1) if numerator % num == 0]
            denominator_F = [num for num in range(1, denominator + 1) if denominator % num == 0]
            gcf = ([a for a in numerator_F for b in denominator_F if a == b])
            
            return (f"-{int(numerator/gcf)}\n {int(denominator/gcf)}")

        else:
            numerator_F = [num for num in range(1, numerator + 1) if numerator % num == 0]
            denominator_F = [num for num in range(1, denominator + 1) if denominator % num == 0]
            gcf = [a for a in numerator_F for b in denominator_F if a == b]

            if (denominator/gcf[-1]) == 1:
                return (f"{int(numerator/gcf[-1])}")

            return (f"\n{int(numerator/gcf[-1])}\n{int(denominator/gcf[-1])}")

num = (fraction(input('Fraction: ')).nums())
print(simplifier(num).simplify())


class Operations: #adds 2 fractions
    def __init__(self, fraction1, fraction2):
        self.fraction1 = fraction1
        self.fraction2 = fraction2

    def add(self):
        numerator1 = self.fraction1[0]
        denominator1 = self.fraction1[1]
        numerator2 = self.fraction2[0]
        denominator2 = self.fraction2[1]

        commondenominator = denominator1 * denominator2
        numerator1 = denominator2 * numerator1
        numerator2 = denominator1 * numerator2
        
        print(f"\n{numerator1}\t{numerator2}\n{commondenominator}\t{commondenominator}")
        return ((numerator1+numerator2), commondenominator)
    
    def subtraction(self):
        numerator1 = self.fraction1[0]
        denominator1 = self.fraction1[1]
        numerator2 = self.fraction2[0]
        denominator2 = self.fraction2[1]

        commondenominator = denominator1 * denominator2
        numerator1 = denominator2 * numerator1
        numerator2 = denominator1 * numerator2
        
        print(f"\n{numerator1}\t{numerator2}\n{commondenominator}\t{commondenominator}")
        return ((numerator1-numerator2), commondenominator)
    
    def multiply(self):
        numerator1 = self.fraction1[0]
        denominator1 = self.fraction1[1]
        numerator2 = self.fraction2[0]
        denominator2 = self.fraction2[1]

        commondenominator = denominator1 * denominator2

        print(f"\n{numerator1}\t{numerator2}\n{denominator1}\t{denominator2}")
        return ((numerator1*numerator2), commondenominator)

    def divide(self):
        numerator1 = self.fraction1[0]
        denominator1 = self.fraction1[1]
        numerator2 = self.fraction2[0]
        denominator2 = self.fraction2[1]

        print(f"\n{numerator1}\t{denominator2}\n{denominator1}\t{numerator2}")
        return ((numerator1*denominator2), denominator1*numerator2)
    
""" Operations
fraction1v1 = fraction(str(input("Fraction1: "))).nums() #input string ex '2/3'
fraction2v1 = fraction(str(input("Fraction2: "))).nums() #input string ex '4/7'


adding = Operations(fraction1v1, fraction2v1).add()
print(simplifier(adding).simplify())


subtract = Operations(fraction1v1, fraction2v1).subtraction()
print(simplifier(subtract).simplify())


multiplying = Operations(fraction1v1, fraction2v1).multiply()
print(simplifier(multiplying).simplify())


division = Operations(fraction1v1, fraction2v1).divide()
print(simplifier(division).simplify())
"""
