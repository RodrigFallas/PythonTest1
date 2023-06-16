import unittest
from temperatura import celsius_a_Fahrenheit

class TestTemperatura(unittest.TestCase):

    def test_celsius_a_fahrenheit(self):

        resultado = celsius_a_Fahrenheit(0)
        self.assertEqual(resultado, 32)

        resultado = celsius_a_Fahrenheit(100)
        self.assertEqual(resultado ,222) #ESTA VA A FALLAR


        if __name__=='__main__':
           unittest.main()
        
