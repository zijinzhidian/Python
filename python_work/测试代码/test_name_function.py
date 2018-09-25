import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatte_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatte_name, 'Janis Joplin')

unittest.main()

###
assertEqual(a, b)      	
assertNotEqual(a, b)   
assertTrue(x)				
assertFalse(x)
assertIn(item, list)
assertNotIn(item, list)
###