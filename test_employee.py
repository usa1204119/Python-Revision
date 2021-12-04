import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """ Testing employee.py """
    def setUp(self):
        self.utkarsh = Employee('Utkarsh','Sharma',95000)
    def test_default_raise(self):
        self.utkarsh.give_raise()
        self.assertEqual(self.utkarsh.salary, 100000)
    def test_custom_raise(self):
        self.utkarsh.give_raise(5000)
        self.assertEqual(self.utkarsh.salary, 100000)
unittest.main()