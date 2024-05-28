#from Prompt_class import prompt

###   determins if the prompted number is float or int   ###

class int_float: 
    def __init__(self, num):
        self.num = num
    
    def int_float(self):
        #rounded = round(math.sqrt(self.num), 1)
        rounded = round(self.num, 1)
        
        if "." in str(self.num):
            for char in range(len(str(self.num))):
                if (str(self.num)[char]) == ".":
                    char = char + 1
                    decimal = (str(self.num)[char:])

                    deci_lis = [n for n in decimal if int(n) > 0]   
                    if len(deci_lis) == 0:
                        return "int"
                    else:
                        return "float"
        else:
            return "int"


