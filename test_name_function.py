import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """ Testing name_function.py """
    def test_first_lastname(self):
        formatted_name = get_formatted_name('Utkarsh','Sharma')
        self.assertEqual(formatted_name,'Utkarsh Sharma')
    
    def test_first_last_middlename(self):
        formatted_name = get_formatted_name('Utkarsh','Sharma','Anurag')
        self.assertEqual(formatted_name,'Utkarsh Anurag Sharma')



unittest.main()