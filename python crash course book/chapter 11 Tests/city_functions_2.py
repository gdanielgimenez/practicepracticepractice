# modified version to make it work with the requirements of the excercise 11.2 page 222
def city_country(city, country, population=''):
    """return a formatted string info city + country"""
    if population:
        full_info = f"{city.title()}, {country.title()} - population {population}"
    else:
        full_info = f"{city.title()}, {country.title()}"
    return full_info
