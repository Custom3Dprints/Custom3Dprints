

#class GreatestCommonFactor():
#    def __init__(self, num1, num2):
#        self.num1 = num1
#        self.num2 = num2
#
#    def gcf(self):
#        factors = [n for n in range(1, self.num1+1) if self.num1 % n == 0]
#        factors2 = [n for n in range(1, self.num2+1) if self.num2 % n == 0]
#        
#        #Common Factors
#        CF = ([a for a in factors for b in factors2 if a == b])
#
#        #Greatest common facotr
#        return int(CF[-1])s
#
#print(GreatestCommonFactor(54, 16).gcf()) 


class GreatestCommonFactor():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def gcf(self):
        #factors = [n for n in range(1, self.nums[for num in nums]+1) if self.num1 % n == 0]
        factor1 = [n for n in range(1, self.num1+1) if self.num1 % n == 0]
        factor2 = [n for n in range(1, self.num2+1) if self.num2 % n == 0]
        
        #Common Factors
        CF = ([a for a in factor1 for b in factor2 if a == b])

        #Greatest common facotr
        return int(CF[-1])

print(GreatestCommonFactor(int(input("num1: ")), int(input("num2: "))).gcf()) 