import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = random.randint(10, 20)

    def attack(self, target):
        damage = self.attack_power
        target.health -= 2*damage
        print(f"{self.name} attacks {target.name} and deals {damage} damage.")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health += heal_amount
        print(f"{self.name} heals themselves for {heal_amount} health.")

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def start_battle(self):
        print("The battle begins!")
        while len(self.players) > 1:
            attacker = random.choice(self.players)
            target = random.choice(self.players)
            if attacker != target:
                attacker.attack(target)
                if target.health <= 0:
                    self.players.remove(target)
                    print(f"{target.name} has been defeated.")
                else:
                    print(f"{target.name} has {target.health} health remaining.")
            else:
                print(f"{attacker.name} tries to attack themselves and fails.")
            print()

        print(f"{self.players[0].name} is the winner!")

# Create players
player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")

# Create game instance
game = Game()

# Add players to the game
game.add_player(player1)
game.add_player(player2)
game.add_player(player3)

# Start the battle
game.start_battle()