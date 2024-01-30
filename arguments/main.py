# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def main():

    print(greet('bob'))

    result = pull(800, 1500, 3)
    print(result)
    #  8.8987e-06 



# Part 1: Greet Template
import re
def greet(name, template = 'Hello, <name>!'):
    if template == 'Hello, <name>!':
        print(f"Hello, {name}!")
        return f"Hello, {name}!"
    else:
        result = (re.sub('<name>', f"{name}", template))
        print(result)
        return result

#  winc answer:
def greet(name, template='Hello, <name>!'):
    return template.replace('<name>', name)

# Part 2: Force
def force(mass, body = 'earth'):
    gravity_of_body = {
        # dictionary serving as lookup table:
        "sun": 274.0,
        "jupiter": 25.0,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6, 
        "pluto": 0.6
    }
    return round(mass * gravity_of_body[body], 1)


# Part 3: Gravity
def pull(m1, m2, d):
    gravitational_constant = 6.674 * 10 ** -11
    gravitational_pull = gravitational_constant *  m1 * m2 / d **2 
    return gravitational_pull


if __name__ == "__main__":

    main()