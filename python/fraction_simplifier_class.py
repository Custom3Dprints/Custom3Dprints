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
                n = n + 1
                denominator = int(self.fraction[n:])
                break
        numerator = int(numerator)
        return (numerator, int(denominator))

class simplifier: #input needed tuple from fraction(nums).simplify() ex: (6,2)
    def __init__(self, fraction):
        self.fraction = fraction
    
    def simplify(self):
        numerator = self.fraction[0]
        denominator = self.fraction[1]
        if numerator < 0: #if numerator is negative
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

            return (f"{int(numerator/gcf[-1])}\n{int(denominator/gcf[-1])}")

#num = (fraction('38/14').nums())
#print(simplifier(num).simplify())
print(simplifier(fraction(str(input('numerator: ')+'/'+str(input('denominator: ')))).nums()).simplify())


"""
ans = fraction("5/-10").nums()

var = simplifier((ans)[0], (ans)[1]).simplify()
print(var)
"""

"""
f = "4/2"
def nums(fraction):
    numerator = ""
    for n in range(len(fraction)):
        if fraction[n] != "/":
            numerator += fraction[n]

        elif fraction[n] == "/":
            n = n + 1
            denominator = int(fraction[n:])
            break
    numerator = int(numerator)
    return (numerator, denominator)
numerator = (nums(f)[0])
denominator = (nums(f)[1])

numerator_F = [num for num in range(1, numerator + 1) if numerator % num == 0]
denominator_F = [num for num in range(1, denominator + 1) if denominator % num == 0]

gcf = []
for i in numerator_F:
    for j in denominator_F:
        if i == j and i not in gcf:
            gcf.append(i)
print(f"{int(numerator/gcf[-1])}\n{int(denominator/gcf[-1])}")
"""