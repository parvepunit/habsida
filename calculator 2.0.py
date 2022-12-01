class Calculator:
    def __init__(self, s):
        self.s = s

    def simple_calculator(self):
        s = self.s
        lst = []
        exp = ""
        digit = []
        count = 0
        ch = ""

        for i in s:
            if i != " ":
                if i.isnumeric() is True:
                    if count < (len(s)-1):
                        ch += i
                        count += 1
                    else:
                        ch += i
                        lst.append(ch)
                        ch = ""
                else:
                    if len(ch) > 0:
                        lst.append(ch)
                    lst.append(i)
                    ch = ""
                    count += 1
            else:
                count += 1
                if len(ch) > 0:
                    lst.append(ch)
                    ch = ""

        for it in lst:
            if it.isnumeric() is True:
                if exp == "/":
                    calc = int(int(digit[-1]) / int(it))
                    digit.pop(-1)
                    digit.append(calc)
                elif exp == "*":
                    calc = int(digit[-1]) * int(it)
                    digit.pop(-1)
                    digit.append(calc)
                elif exp == "+":
                    calc = 0 + int(it)
                    digit.append(calc)
                elif exp == "-":
                    calc = 0 - int(it)
                    digit.append(calc)
                else:
                    digit.append(int(it))
            else:
                exp = it
        result = 0
        for j in digit:
            result += j
        return result

calc = Calculator("3+2")
print(calc.simple_calculator())
    