def city_country(city,country,population=''):
    if population:
        return(city.title() + ', ' + country.title() + '-' + str(population))        
    else:
        return(city.title()+', '+country.title())