import unittest
import day01, day02, day03, day04, day05
import day06, day07, day08, day09, day10
import day11, day12, day13, day14, day15
import day16, day17, day18, day19

class TestAoC2020(unittest.TestCase):

    def gen_test(self, day, expected):
        fun = f"day{day}.main('../input/input{day}.txt')"
        result = eval(fun)
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[1], expected[1])
    
    def test_day01(self):
        self.gen_test('01', [138379, 85491920])
    
    def test_day02(self):
        self.gen_test('02', [439, 584])
    
    def test_day03(self):
        self.gen_test('03', [207, 2655892800])
    
    def test_day04(self):
        self.gen_test('04', [230, 156])
    
    def test_day05(self):
        self.gen_test('05', [842, 617])
    
    def test_day06(self):
        self.gen_test('06', [6633, 3202])
    
    def test_day07(self):
        self.gen_test('07', [103, 1469])
    
    def test_day08(self):
        self.gen_test('08', [1137, 1125])
    
    def test_day09(self):
        self.gen_test('09', [1038347917, 137394018])
        
    def test_day10(self):
        self.gen_test('10', [1755, 4049565169664])

    def test_day11(self):
        self.gen_test('11', [2222, 2032])
    
    def test_day12(self):
        self.gen_test('12', [1010, 52742])
    
    def test_day13(self):
        self.gen_test('13', [2298, 783685719679632])
    
    def test_day14(self):
        self.gen_test('14', [3059488894985, 2900994392308])
    
    def test_day15(self):
        self.gen_test('15', [639, 266])
    
    def test_day16(self):
        self.gen_test('16', [25916, 2564529489989])

    def test_day17(self):
        self.gen_test('17', [252, 2160])

    def test_day18(self):
        self.gen_test('18', [6811433855019, 129770152447927])

    def test_day19(self):
        self.gen_test('19', [248, 381])

if __name__ == '__main__':
    unittest.main()
