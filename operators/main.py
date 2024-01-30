# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#exercise 1
spain_language_most_spoken = 'spanish'
switzerland_language_most_spoken = 'german'
print(spain_language_most_spoken != switzerland_language_most_spoken) # imho: == makes more sense here!

#exercise 2
spain_religion = 'roman_catholic'
switzerland_religion = 'roman_catholic'
print(spain_religion == switzerland_religion)

#exercise 3
spain_capital_word_length = len('madrid')
switzerland_capital_word_length = len('bern')
print(spain_capital_word_length != switzerland_capital_word_length)

#exercise 4
spain_gdp = 1393351 * 10 ** 6     # 2019 est.
switzerland_gdp = 731502 * 10 * 6 # 2019 est.
print(switzerland_gdp > spain_gdp)  

#exercise 5
spain_population_growth_rate = -0.03
switzerland_population_growth_rate = 0.65
print(spain_population_growth_rate < 1 and switzerland_population_growth_rate < 1)

#exercise 6
spain_population_count = 47260584 #(July 2021 est.)
switzerland_population_count = 8453550 #(July 2021 est.)
print(spain_population_count > 10000000 or switzerland_population_count > 10000000)

#exercise 7
spain_population_count2 = 47260584 #(July 2021 est.)
switzerland_population_count2 = 8453550 #(July 2021 est.)
print(bool(spain_population_count2 > 10000000) != bool(switzerland_population_count2 > 10000000))

