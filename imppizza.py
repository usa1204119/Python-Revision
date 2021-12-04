# importing an entire module
import pizza1
pizza1.make_pizza(12,'pineapple')
# importing specific functions
from pizza1 import make_pizza
make_pizza(12,'pepperoni')
# using as to give a function an alias
from pizza1 import make_pizza as mp 
mp(12,'mushroom')
# using as to give a module an alias
import pizza1 as p
p.make_pizza(12,'extra cheese')

from pizza import *
utkarsh = build_person('Utkarsh','Sharma',location='Boisar',field='Science')

from greet import greet_users as g
g('Shivam')
