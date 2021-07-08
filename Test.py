class Test(unittest.TestCase):
    def test_add(self):
        c = Calculator()
        c.clear()
        c.add_character("1")
        c.add_character("+")
        c.add_character("1")
        c.equal()

        self.assertEqual("2", c.calculation)
    def test_sub(self):
        c = Calculator()
        c.clear()
        c.add_character("1")
        c.add_character("-")
        c.add_character("1")
        c.equal()

        self.assertEqual("0", c.calculation)
    def test_multiply(self):
        c = Calculator()
        c.clear()
        c.add_character("5")
        c.add_character("*")
        c.add_character("5")
        c.equal()

        self.assertEqual("25", c.calculation)  
    def test_divide(self):
        c = Calculator()
        c.clear()
        c.add_character("25")
        c.add_character("/")
        c.add_character("5")
        c.equal()

        self.assertEqual("5", c.calculation)   
    def test_pemdas(self): # 25/5 + 5 * 55 
        c = Calculator()
        c.clear()
        c.add_character("25")
        c.add_character("/")
        c.add_character("5")
        c.add_character("+")
        c.add_character("5")
        c.add_character("*")
        c.add_character("5")
        c.add_character("5")
        c.equal()

        self.assertEqual("280", c.calculation)   
if __name__ == "__main__":
    unittest.main()
