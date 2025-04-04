#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_b.question_b import get_day_of_the_week

class Test_Config(unittest.TestCase):

    def test_get_day_of_the_week(self):
        self.assertEqual (get_day_of_the_week(0), "Invalid number")
        self.assertEqual (get_day_of_the_week(1), "Monday")
        self.assertEqual (get_day_of_the_week(2), "Tuesday")
        self.assertEqual (get_day_of_the_week(3), "Wednesday")
        self.assertEqual (get_day_of_the_week(8), "Invalid number")
