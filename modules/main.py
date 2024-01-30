# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# task 1:
import this  # pitfall: just importing is enough...no need to do print(this)

import time, math, datetime, sys
from greet import supergreeting

def main():
    
# task 4:
    result = iso_now()
    print(result)

# task 5:
    result = platform()
    print(result)


# task 2:
def wait(seconds): 
    time.sleep(seconds)    # jsComp: e.g. setTimeout()

# task 3:
def my_sin(radians):
    return math.sin(radians)


def iso_now():
    return  datetime.datetime.now().isoformat(timespec='minutes')  # jsComp: data-time-stuff is messy in  vanilla js.

def platform():
    return sys.platform

# task 6:
def supergreeting_wrapper(name):
    return supergreeting(name)




# datetime.now("%Y-%m-%dT%H:%M")

if __name__ == "__main__":

    main()