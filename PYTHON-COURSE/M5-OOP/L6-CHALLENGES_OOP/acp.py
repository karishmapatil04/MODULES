class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        num = self.number
        roman = ""

        for i in range(len(val)):
            while num >= val[i]:
                roman += syb[i]
                num -= val[i]

        return roman


# Create object
n = IntegerToRoman(58)

# Display result
print("Integer:", n.number)
print("Roman Numeral:", n.convert())