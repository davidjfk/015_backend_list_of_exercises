# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
broccoli = 2
brussel_sprout = 7
leek = 2
potato = 3


sum_one_each = broccoli + brussel_sprout + leek + potato 

avg_price = sum_one_each / 4


num_broccolis = 5
num_brussel_sprouts = 10
num_leeks = 2
num_potatoes = 7

sum_total =  broccoli * num_broccolis + brussel_sprout * num_brussel_sprouts + leek * num_leeks + potato * num_potatoes

# print(sum_total )
# print(type(sum_total))

discount_percentage = 30

discounted_sum_total = sum_total * (100 - discount_percentage ) / 100 
# alternative: discounted_sum_total = sum_total - sum_total * discount_percentage / 100
discounted_sum_total = round (discounted_sum_total, 2)

print(discounted_sum_total )
# print(type(discounted_sum_total))