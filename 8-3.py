def make_tshirt(size,message):
    print('I want a ' + str(size) + 'cm tshirt. With the message, "'
    + message + '" printed on it.')
make_tshirt(34,'HAPPY ME')
make_tshirt(size=34, message='BE THE CHANGE YOU WANT TO SEE IN THE WORLD')


# Large shirts
def make_tshirt(message,size='large'):
    print('I want a ' + str(size) + ' tshirt. With the message, "'
          + message + '" printed on it.')

make_tshirt('I love python')
make_tshirt('Data Scientist',size='medium')
make_tshirt('Earning in 6 figures',size='extra large')


# city
def describe_city(city_name,country='India'):
    print(city_name.title() + ' is in ' + country.title() + '.')
describe_city('Mumbai')
describe_city('Bangalore')
describe_city('las Vegas',country='USA')