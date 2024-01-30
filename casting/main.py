# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1
leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

# Part 2
order = 'leek 4'
index_of_number_of_leek = order.find('4')
number_of_leek = int(order[index_of_number_of_leek:])
sum_total = number_of_leek * leek_price
print(sum_total)

# Part 3
#expected output: 3.74e
broccoli_price_per_kg_in_euro = 2.34
broccoli_order_in_kg = 1.6
total_price = broccoli_price_per_kg_in_euro * broccoli_order_in_kg

total_price_scientific_notation = "{:.2e}".format(round(total_price, 2)) #actual output: 3.74e+00  (wincpy does not like this)

total_price_scientific_notation = round(total_price, 2) #actual output: 3.74  (wincpy does not like this)

print(str(broccoli_order_in_kg) + 'kg broccoli costs ' + str(total_price_scientific_notation))    #remark: fstring is easier.

