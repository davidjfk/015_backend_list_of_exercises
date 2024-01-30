from itertools import count
from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

def main():


    unique_koala_facts(7)
    
   
    num_joey_facts()



    koala_weight()

def unique_koala_facts(number_of_unique_koala_facts):
    if number_of_unique_koala_facts > 1000:
        return
    max_nr_of_iterations = 1000
    iteration_count = 0
    target_list_with_unique_koala_facts = []
    bladie = 0
    while bladie < number_of_unique_koala_facts and iteration_count < max_nr_of_iterations:
        var_with_koala_fact = random_koala_fact()
        if var_with_koala_fact not in target_list_with_unique_koala_facts:
            target_list_with_unique_koala_facts.append(var_with_koala_fact)
            print('appended')
            bladie += 1
            iteration_count += 1
            print(bladie)

        else: iteration_count += 1
        print(f"number_of_unique_koala_facts: {number_of_unique_koala_facts}")
        print('bla')
    return target_list_with_unique_koala_facts



def num_joey_facts():
    list_with_facts_that_contain_joey = []
    number_of_facts_mentioning_term_joey = 0
    count_of_first_random_koala_fact = 1
    first_random_koala_fact = random_koala_fact()
    print(f"first_random_koala_fact: {first_random_koala_fact}")
    if "joey" in first_random_koala_fact:
        number_of_facts_mentioning_term_joey += 1
        list_with_facts_that_contain_joey.append(first_random_koala_fact)
    while count_of_first_random_koala_fact < 10:
        next_random_koala_fact = random_koala_fact()
        if next_random_koala_fact not in list_with_facts_that_contain_joey and next_random_koala_fact != first_random_koala_fact:
            if "joey" in next_random_koala_fact:
                number_of_facts_mentioning_term_joey += 1
                list_with_facts_that_contain_joey.append(next_random_koala_fact)
                print(f"list_with_facts_that_contain_joey: {list_with_facts_that_contain_joey}")
        elif next_random_koala_fact == first_random_koala_fact:
            count_of_first_random_koala_fact += 1
    print(f"count_joey: {number_of_facts_mentioning_term_joey}")
    print(f"count_first_rand_koala_fact: {count_of_first_random_koala_fact}")
    return number_of_facts_mentioning_term_joey

def koala_weight():
    return 14





if __name__ == "__main__":
    # print(random_koala_fact())

    main()




