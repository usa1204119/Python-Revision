class Employee():
    """ A class representing employee """
    def __init__(self,f_name,l_name,salary):
        """ defining name and salary """
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.salary = salary

    def give_raise(self,amount=5000):
        """ giving raise to salary """
        self.salary += amount