def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    great_magicians = []
    while magicians:
        current = magicians.pop()
        great_magician = current + ' the great.'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians
magicians = ['David','caroline','Teller']
show_magicians(magicians)
great_magician = make_great(magicians[:])
show_magicians(great_magician)
show_magicians(magicians)