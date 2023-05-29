def get_capital(country):
    europe_capitals = {
        'albania': 'tirana',
        'andorra': 'andorra la vella',
        'austria': 'vienna',
        'belarus': 'minsk',
        'belgium': 'brussels',
        'bosnia and herzegovina': 'sarajevo',
        'bulgaria': 'sofia',
        'croatia': 'zagreb',
        'cyprus': 'nicosia',
        'czech republic': 'prague',
        'denmark': 'copenhagen',
        'estonia': 'tallinn',
        'finland': 'helsinki',
        'france': 'paris',
        'germany': 'berlin',
        'greece': 'athens',
        'hungary': 'budapest',
        'iceland': 'reykjavik',
        'ireland': 'dublin',
        'italy': 'rome',
        'kosovo': 'pristina',
        'latvia': 'riga',
        'liechtenstein': 'vaduz',
        'lithuania': 'vilnius',
        'luxembourg': 'luxembourg city',
        'malta': 'valletta',
        'moldova': 'chisinau',
        'monaco': 'monaco',
        'montenegro': 'podgorica',
        'netherlands': 'amsterdam',
        'north macedonia': 'skopje',
        'norway': 'oslo',
        'poland': 'warsaw',
        'portugal': 'lisbon',
        'romania': 'bucharest',
        'russia': 'moscow',
        'san marino': 'san marino',
        'serbia': 'belgrade',
        'slovakia': 'bratislava',
        'slovenia': 'ljubljana',
        'spain': 'madrid',
        'sweden': 'stockholm',
        'switzerland': 'bern',
        'turkey': 'ankara',
        'ukraine': 'kyiv',
        'united kingdom': 'london',
        'vatican city': 'vatican city',
    }

    country = country.lower()

    if country in europe_capitals:
        return europe_capitals[country]
    else:
        return "Capital information not found for that country."

user_country = input("Enter the name of a country in Europe: ")
capital = get_capital(user_country)

print(f"The capital city of {user_country} is {capital}.\n")
print("Run the program for another country")
