class RomanNum():
    def roman(self, num):

        romanNumber = ""
        n = num%10
        nDecimal = int(num%100/10)
        nHund = int(num%1000/100)
        nThou = int(num % 10000 / 1000)

        if nThou == 1:
            romanNumber += "M"
        if nThou == 2:
            romanNumber += "MM"
        if nThou == 3:
            romanNumber += "MMM"



        if nHund == 1:
            romanNumber += "C"
        elif nHund == 2:
            romanNumber += "CC"
        elif nHund == 3:
            romanNumber += "CCC"
        elif nHund == 4:
            romanNumber += "CD"
        elif nHund == 5:
            romanNumber += "D"
        elif nHund == 6:
            romanNumber += "DC"
        elif nHund == 7:
            romanNumber += "DCC"
        elif nHund == 8:
            romanNumber += "DCCC"
        elif nHund == 9:
            romanNumber += "CM"

        if nDecimal == 1:
            romanNumber += "X"
        elif nDecimal == 2:
            romanNumber += "XX"
        elif nDecimal == 3:
            romanNumber += "XXX"
        elif nDecimal == 4:
            romanNumber += "XL"
        elif nDecimal == 5:
            romanNumber += "L"
        elif nDecimal == 6:
            romanNumber += "LX"
        elif nDecimal == 7:
            romanNumber += "LXX"
        elif nDecimal == 8:
            romanNumber += "LXXX"
        elif nDecimal == 9:
            romanNumber += "XC"

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