from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
def main():

    shortest_names(countries)

    most_vowels(countries)

   
    # argument 1: list with sorted countries( longest ones first)
    list_with_sorted_countries = sort_countries_on_name_length(countries, False)
    print(list_with_sorted_countries)

    countries_that_form_alphabet = alphabet_set(list_with_sorted_countries)
    # with countries as argument, I need 14 countries to form the alphabet. 14 is good enough according to specs. But with list_with_sorted_countries I need only 9 countries. 
    print(f"countries_that_form_alphabt: {countries_that_form_alphabet}")


'''

shortest_names: takes a list of country names and returns a list of country names that have the shortest length.

If there is only one country with the shortest name the list will contain only that country's name, 
otherwise multiple countries should be in the list. Use a for-loop and len!

'''

def shortest_names(countries):
    list_with_shortest_names = []
    length_of_shortest_country_name = 100 # 100 is bigger than longest country name.
    for country in countries:
        if len(country) < length_of_shortest_country_name:
            list_with_shortest_names.clear()
            list_with_shortest_names.append(country)
            length_of_shortest_country_name = len(country)
        elif len(country) == length_of_shortest_country_name:
            list_with_shortest_names.append(country)
    return list_with_shortest_names

'''
most_vowels: takes a list of country names and returns a list with the top three countries that have the most vowels in their name.

The country with the most vowels should be on position 0 in the list, the country with the second-most on position 1, and so on. 

If there are multiple countries with the same number of vowels the order does not matter. To sidestep the y-issue: we count aeiou as vowels.

'''

def most_vowels(countries):
    list_with_three_countries_with_most_vowels_in_name = []
    # print(list_with_three_countries_with_most_vowels_in_name)
    country_list_sorted = sorted(countries, key=lambda country: sum(vowel in 'aeiou' for vowel in country.lower()), reverse=True)
    list_with_three_countries_with_most_vowels_in_name.append(country_list_sorted[0])
    list_with_three_countries_with_most_vowels_in_name.append(country_list_sorted[1])
    list_with_three_countries_with_most_vowels_in_name.append(country_list_sorted[2])
    return list_with_three_countries_with_most_vowels_in_name

def sort_countries_on_name_length(countries, sortAscending):
    country_list_sorted = sorted(countries, key=len, reverse= not(sortAscending))
    return country_list_sorted

#  create_list_with_country_names_whose_letters_form_alphabet 
def alphabet_set(countries):
    alphabet = listAlphabet()
    # wincpy only accepts 1 argument. Otherwise 'alphabet' would be a fn argument too (imho)
    list_with_country_names_whose_letters_form_alphabet = []
    for country in countries:
        number_of_vowels_in_country_that_match_still_unmatched_vowels_in_alphabet = 0
        my_country = list(country.lower())
        print(my_country)
        for vowel in my_country:
            if vowel in alphabet:
                alphabet.remove(vowel)
                number_of_vowels_in_country_that_match_still_unmatched_vowels_in_alphabet += 1
        if number_of_vowels_in_country_that_match_still_unmatched_vowels_in_alphabet > 0:
            list_with_country_names_whose_letters_form_alphabet.append(country)
    return list_with_country_names_whose_letters_form_alphabet       



'''
alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet.

How short can you get your list to be?

Letter case is not relevant, so 'a' is the same letter as 'A' with regards to the alphabet.
Solutions with 14 or fewer countries are accepted as correct.

'''

#  create list with comma separated alphabet letters "a-z"
def listAlphabet():
  return list(map(chr, range(97, 123)))


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    main()




################################################








