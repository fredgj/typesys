import unittest

from typesys import type_corrector, type_hints, return_type, returns


######################################################
# Functions for testing the type corrector decorator #
######################################################


@type_corrector(int, int)
def add(a, b=0):
    return a+b


@type_corrector(int)
def mult(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


@type_corrector(int)
def kw_mult(**kwargs):
    first = kwargs.get('first')
    second = kwargs.get('second')
    third = kwargs.get('third')
    
    return first * second * third


######################################################
# End type corrector test functions                  #
######################################################


class TypeCorrectorTest(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(add('1', 2), 3)

    def test_add3(self):
        self.assertEqual(add('1', '2'), 3)
    
    def test_add4(self):
        self.assertEqual(add(1, b=2), 3)

    def test_add5(self):
        self.assertEqual(add('1', b=2), 3)

    def test_add6(self):
        self.assertEqual(add('1', b='2'), 3)

    def test_mult1(self):
        self.assertEqual(mult(2, 3, 4), 24)
    
    def test_mult2(self):
        self.assertEqual(mult('2', 3, 4), 24)  
    
    def test_mult3(self):
        self.assertEqual(mult('2', '3', 4), 24)  
    
    def test_mult4(self):
        self.assertEqual(mult('2', '3', '4'), 24)

    def test_kw_mult1(self):
        self.assertEqual(kw_mult(first=2, second=3, third=4), 24)
    
    def test_kw_mult2(self):
        self.assertEqual(kw_mult(first='2', second=3, third=4), 24)
    
    def test_kw_mult3(self):
        self.assertEqual(kw_mult(first='2', second='3', third=4), 24)
    
    def test_kw_mult4(self):
        self.assertEqual(kw_mult(first='2', second='3', third='4'), 24)


######################################################
# Functions for testing the type hinting decorator   #
######################################################


@type_hints(int, int)
def hint_add(a, b):
    """Adds two numbers"""
    return a+b


@type_hints(int, int)
def def_add(a, b=0):
    return a+b


@type_hints(int, float)
def hint_mult(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


@type_hints(int, float)
def hint_kw_mult(**kwargs):
    first = kwargs.get('first')
    second = kwargs.get('second')
    third = kwargs.get('third')    
    return first * second * third


######################################################
# End type hinting test functions                    #
######################################################


class TypeHintingTest(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(hint_add(1,2), 3)

    def test_add_error(self):
        self.assertRaises(TypeError, hint_add(1,'2'))

    def test_def_add1(self):
        self.assertEqual(def_add(1,b=2), 3)

    def test_def_add_error(self):
        self.assertRaises(TypeError, def_add(1,b='2'))

    def test_mult1(self):
        self.assertEqual(hint_mult(2,3,4), 24)

    def test_mult2(self):
        self.assertEqual(hint_mult(2,3,4.5), 27)

    def test_mult_error(self):
        self.assertRaises(TypeError, mult(2,3,'4'))

    def test_kw_mult1(self):
        self.assertEqual(hint_kw_mult(first=2, second=3, third=4), 24)

    def test_kw_mult2(self):
        self.assertEqual(hint_kw_mult(first=2, second=3, third=4.5), 27)

    def test_kw_mult_error(self):
        self.assertRaises(TypeError, hint_kw_mult(first=2, second=3, third='4'))


######################################################
# Functions for testing the return type decorator    #
######################################################


@return_type(int, float)
def ret_add(x,y):
    return x+y


@return_type(int)
def strict_ret_add(x,y):
    return x+y


######################################################
# End return type test functions                     #
######################################################


class ReturnTypeTest(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(ret_add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(ret_add(1.5, 2.5), 4)

    def test_add_error(self):
        self.assertRaises(Exception, ret_add(1,'2'))

    def test_strict_add1(self):
        self.assertEqual(strict_ret_add(1, 2), 3)

    def test_strict_add_error(self):
        self.assertRaises(TypeError, strict_ret_add(1,2.0))


########################################################
# Functions for testing the return corrector decorator #
########################################################


@returns(str)
def returns_add(x,y):
    return x+y


######################################################
# End return type test functions                     #
######################################################


class ReturnTypeCorrectorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(returns_add(1,2), '3')

    def test_add_type(self):
        self.assertEqual(type(returns_add(1,2)), str)


if __name__ == '__main__':
    unittest.main()

