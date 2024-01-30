# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

def greet(name):
    return 'Hello, ' + name +'!'

print(greet('Bob'))



def add(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

print(add(5,3,2))



def positive(number):
    if number > 0:
        return True
    return False

positive(10)

# winc solution:
'''
def positive(number):
  return number > 0
'''

def negative(number):
    if number < 0:
        return True
    return False

negative(10)
