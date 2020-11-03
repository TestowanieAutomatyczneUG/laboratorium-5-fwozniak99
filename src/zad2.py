class RomanNum():
    def roman(self, num):

        romanNumber = ""
        n = num%10
        nDecimal = int(num%100/10)


        if nDecimal == 1:
            romanNumber += "X"
        if nDecimal == 2:
            romanNumber += "XX"
        if nDecimal == 3:
            romanNumber += "XXX"
        if nDecimal == 4:
            romanNumber += "XL"

        if n==1:
            romanNumber += "I"
        elif n==2:
            romanNumber += "II"
        elif n==3:
            romanNumber += "III"
        elif n==4:
            romanNumber += "IV"
        elif n==5:
            romanNumber += "V"
        elif n==6:
            romanNumber += "VI"
        elif n == 7:
            romanNumber += "VII"
        elif n == 8:
            romanNumber += "VIII"
        elif n==9:
            romanNumber += "IX"


        return romanNumber