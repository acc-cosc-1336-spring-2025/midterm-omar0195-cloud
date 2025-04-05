#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_b.question_b import get_day_of_the_week
from src.question_c.question_c import use_global, get_global_num
from src.question_d.question_d import get_assessment_value, get_tax_assessed

class Test_Config(unittest.TestCase):

    def test_get_day_of_the_week(self):
        self.assertEqual (get_day_of_the_week(0), "Invalid number")
        self.assertEqual (get_day_of_the_week(1), "Monday")
        self.assertEqual (get_day_of_the_week(2), "Tuesday")
        self.assertEqual (get_day_of_the_week(3), "Wednesday")
        self.assertEqual (get_day_of_the_week(8), "Invalid number")

    def test_use_global(self):
        self.assertEqual(get_global_num(), 25, "Initial value of value of global_num is 25")
        use_global()
        self.assertEqual(get_global_num(), 10, "Global_num should be 10 now") 

    def test_get_assessment_value(self):
        self.assertEqual(get_assessment_value(10000), 6000)
        self.assertEqual(get_assessment_value(20000), 12000)
    
    def test_get_tax_assessed(self):
        self.assertAlmostEqual(get_tax_assessed(6000), 43.20, places= 2)
        self.assertAlmostEqual(get_tax_assessed(10000), 72.00, places= 2)