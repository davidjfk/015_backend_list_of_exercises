# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# assignment 1: fn alphabetical order
films = ["zorro", "alpha", "dexter"]

def alphabetical_order(film_names):
    film_names_sorted = sorted(film_names)
    return film_names_sorted

result = alphabetical_order(films)
print(result)

# assignment 2: fn won_golden_globe
def won_golden_globe(movie_name):
    movies_of_John_Williams_winning_golden_globe_award = ["Jaws".lower(), "Star Wars: Episode IV – A New Hope".lower(), "E.T. the Extra-Terrestrial".lower(), "Memoirs of a Geisha".lower() ]
    
    if (movie_name.lower()) in movies_of_John_Williams_winning_golden_globe_award:
        return True
    else:
        return False

has_won_a_golden_globe_award1 = won_golden_globe("Forrest Gump")
print(has_won_a_golden_globe_award1)

has_won_a_golden_globe_award2 = won_golden_globe("Jaws")
print(has_won_a_golden_globe_award2)



# assignment 3: remove_toto_albums

toto_albums = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between", "35th Anniversary - Live in Poland", "Toto XIV", "Old is New", "40 Tours Around the Sun", "With a Little Help from My Friends"]
# toto_albums = ["a", "b"]

def make_list_lower_case (list):
    for i in range(len(list)):
        list[i] = list[i].lower()
    return list

toto_albums_lower_case = make_list_lower_case(toto_albums)
print(toto_albums_lower_case)

def remove_toto_albums(movie_list):

    movie_list2 = movie_list
    for album in movie_list2:
        for album in movie_list2:
            if album in toto_albums_lower_case:
                movie_list2.remove(album)

    return movie_list2

albums_of_toto_john_and_others = ["Jaws","The Seventh One", "Fahrenheit", "The Seventh One", "Toto XX", "book", "Falling in Between", "Miami Vice", "35th Anniversary - Live in Poland", "Seven Seas", "Toto XIV", "Old is New", "40 Tours Around the Sun", "With a Little Help from My Friends"]

albums_of_toto_john_and_others_lower_case = make_list_lower_case(albums_of_toto_john_and_others)
print(albums_of_toto_john_and_others_lower_case)


albums_without_toto = remove_toto_albums( albums_of_toto_john_and_others_lower_case)
print(albums_without_toto)



