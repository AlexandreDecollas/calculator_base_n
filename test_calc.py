from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def test_convert_173_base_10_in_255_base_8(self):
        self.calc: Calc = Calc()
        result: str = self.calc.convertNumber(173, 10, 8)
        self.assertEqual('255', result)

    def test_convert_173_base_8_in_173_base_8(self):
        self.calc: Calc = Calc()
        result: str = self.calc.convertNumber(173, 8, 8)
        self.assertEqual('173', result)

    def test_convert_173_base_10_in_10101101_base_2(self):
        self.calc: Calc = Calc()
        result: str = self.calc.convertNumber(173, 10, 2)
        self.assertEqual('10101101', result)

    def test_convert_88_base_10_in_107_base_9(self):
        self.calc: Calc = Calc()
        result: str = self.calc.convertNumber(88, 10, 9)
        self.assertEqual('107', result)

    def test_convert_88_base_9_in_80_base_10(self):
        self.calc: Calc = Calc()
        result: str = self.calc.convertNumber(88, 9, 10)
        self.assertEqual('80', result)

    def test_add_88_plus_8_in_base_9(self):
        self.calc: Calc = Calc()
        result: str = self.calc.add2Numbers(88, 8, 9)
        self.assertEqual('107', result)

    def test_add_8_plus_88_in_base_9(self):
        self.calc: Calc = Calc()
        result: str = self.calc.add2Numbers(8, 88, 9)
        self.assertEqual('107', result)

    def test_add_by_list_88_plus_8_plus_8_in_base_9(self):
        self.calc: Calc = Calc()
        result: str = self.calc.addByList([88, 8], 9)
        self.assertEqual('107', result)

    def test_add_by_list_8_plus_88_plus_8_in_base_9(self):
        self.calc: Calc = Calc()
        result: str = self.calc.addByList([8, 88], 9)
        self.assertEqual('107', result)
