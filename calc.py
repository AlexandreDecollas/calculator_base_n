import math


class Calc:

    def add2Numbers(self, num1: int, num2: int, base: int) -> str:
        num1Dec: str = self.convertNumber(num1, base, 10)
        num2Dec: str = self.convertNumber(num2, base, 10)
        resDec: int = int(num1Dec) + int(num2Dec)
        return self.convertNumber(resDec, 10, base)

    def addByList(self, numbers: list, base: int) -> str:
        resDec: int = 0

        for number in numbers:
            decNumber: str = self.convertNumber(number, base, 10)
            resDec: int = resDec + int(decNumber)

        return self.convertNumber(resDec, 10, base)

    def convertNumber(self, number: int, startBase: int, endBase: int) -> str:
        if startBase == endBase:
            return str(number)

        if startBase != 10:
            return self.__getDecimalValue(number, startBase)

        range: int = self.__getUnderRange(endBase, number)
        res: str = self.__getConvertionByAlgoBySuppr(endBase, range, number)
        return res

    def __getConvertionByAlgoBySuppr(self, endBase, range, remaining) -> str:
        res: str = ''

        while range >= 1:
            divider: int = math.floor(remaining / (endBase ** range))
            res += str(divider)
            remaining -= (endBase ** range) * divider
            range -= 1

        res += str(remaining)
        return res

    def __getUnderRange(self, endBase, remaining) -> int:
        range: int = 0

        while endBase ** range <= remaining:
            range += 1

        return range - 1

    def __getDecimalValue(self, number: int, startBase: int) -> str:
        stringValue: str = str(number)
        stringValues: list = list(stringValue)
        length: int = len(stringValue)
        res: int = 0

        exp: int = length - 1
        for value in stringValues:
            res += (int(value)) * (startBase ** exp)
            exp -= 1

        return str(res)
