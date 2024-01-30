class Player:
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        if not 0 <= speed <= 1:
            raise ValueError("speed must be between 0 and 1")
        self.speed = speed
        if not 0 <= endurance <= 1:
            raise ValueError("endurance must be between 0 and 1")
        self.endurance = endurance
        if not 0 <= accuracy <= 1:
            raise ValueError("accuracy must be between 0 and 1")
        self.accuracy = accuracy

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."


    def strength(self):
        speed = self.speed
        endurance = self.endurance
        accuracy = self.accuracy

        highest = max(speed, endurance, accuracy)

        if speed == endurance == accuracy == highest:
            return 'speed', self.speed
        elif speed == endurance == highest:
            return 'speed', self.speed
        elif speed == accuracy == highest:
            return 'speed', self.speed
        elif endurance == accuracy == highest:
            return 'endurance', self.endurance
        elif speed == highest:
            return 'speed', self.speed
        elif endurance == highest:
            return 'endurance', self.endurance
        elif accuracy == highest:
            return 'accuracy', self.accuracy
        else:
            print("Class Player: Error in method strength()")

gullit = Player('Gullit', 0.88, 0.71, 0.93)
print(gullit.introduce())
print('The strength of ' + str(gullit.name) + 'is: ' + str(gullit.strength()[1]) + ".")

class Commentator():
    def __init__(self, fullName):
        self.fullName = fullName
        self.name = fullName.split(' ')[0] + ' ' + fullName.split(' ')[1]
        # fooling around with split:
        self.firstName_with_first_letter_of_lastName = fullName.split(' ')[0] + ' ' + fullName.split(' ')[1][0] + '.'

# correct answer (after interacting with wincpy):

class Commentator():
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return player.speed + player.endurance + player.accuracy    
    
    def compare_players(self, player1, player2, strength):
        strength_player_1 = getattr(player1, strength)
        strength_player_2 = getattr(player2, strength)

        if player1.strength()[1] > player2.strength()[1]:
            return player1.name
        elif  player1.strength()[1] < player2.strength()[1]:
            return player2.name
        elif player1.strength()[1] == player2.strength()[1]:
            print('-----------')
            print(player1.strength()[1])
            print(player2.strength()[1])
            if self.sum_player(player1) > self.sum_player(player2):
                return player1.name
            elif self.sum_player(player1) < self.sum_player(player2):
                return player2.name
            else:
                return 'These two players might as well be twins!'
 

    

ray = Commentator('Ray Hudson')
print(ray.name)
print(ray.sum_player(gullit))

messi = Player('Messi', 0.66, 0.85, 0.72)
xavi = Player('Xavi', 0.66, 0.96, 0.62)

zidane = Player('Zidane', 0.74, 0.92, 0.88) # same sum_player and strength as ronaldo.
ronaldo = Player('Ronaldo', 0.74, 0.92, 0.88) # same sum_player value as van_basten
van_basten = Player('Marco van basten', 0.92, 0.74, 0.88) # strength (i.e. speed) of van_basten is higher than ronaldo
pele = Player('Pele', 0.97, 0.70, 0.93)
maradona = Player('Maradona', 0.94, 0.70, 0.95)




players = [gullit, messi, zidane, ronaldo, van_basten, pele, maradona]
for player in players: 
    print(player.name + ' has a sum of: ' + str(ray.sum_player(player)))
    print(player.name + ' has a strength of: ' + str(player.strength()[1]) + ".")
    print('-----------')

print(ray.compare_players(messi, maradona, 'speed')) # expected output: messi


print(ray.compare_players(van_basten, pele, 'accuracy')) # expected output: pele


print(ray.compare_players(messi, xavi, 'speed')) 
'''
expected output: xavi
reason:
both have same speed, but xavi has higher endurance.
'''

print(ray.compare_players(ronaldo, zidane, 'speed')) 
'''
expected output: 'These two players might as well be twins!'
reason:
Both players have same sum_player value and same strength value
'''

