import pokemon as pokemod

class Trainer:

    def __init__(self, name, pokemon, levels, types, potions, revives):
        self.name = name
        self.pokemon_names = pokemon
        self.pokemon = []
        self.potions = potions
        self.revives = revives
        self.currently_active = 0
        # Create Pokemon instances for each pokemon
        for i in range(len(pokemon)):
            self.pokemon.append(pokemod.Pokemon(self.name + "s' " + pokemon[i], levels[i], types[i], False))

    # Method for using potions NEEDS TO BE UPDATED ONLY WORKS ON CHARMANDERS :p
    def use_potion(self, pokemon = "Charmander"):
        if self.potions != 0:
            print(self.name + " used a potion")
            found = False
            for i in range(len(self.pokemon)):
                if self.pokemon[i].name == self.name + "s' " + str(pokemon):
                    self.pokemon[i].gain_health(20)
                    self.potions -= 1
                    found = True
            if found == False:
                print("Invalid pokemon")
        else:
            print(self.name + " has no potions remaining.")
    
    # Method for using a revive
    def use_revive(self, pokemon):
        if self.revives != 0:
            print(self.name + " used a revive")
            found = False
            for i in range(len(self.pokemon)):
                if self.pokemon[i].name == self.name + "s' " + str(pokemon):
                    self.pokemon[i].revive()
                    self.revives -= 1
                    found = True
            if found == False:
                print("Invalid pokemon")
        else:
            print(self.name + " has no revives remaining.")

    # Method for trainer attacking another trainer
    def trainer_attack(self, trainer):
        self.pokemon[self.currently_active].attack(trainer.pokemon[trainer.currently_active])

    # Method for switching active pokemon
    def switch(self, pokemon):
        found = False
        print(self.name + " switches out " + self.pokemon_names[self.currently_active] + ".")
        for i in range(len(self.pokemon)):
            if self.pokemon[i].name == self.name + "s' " + str(pokemon):
                self.currently_active = i
                found = True
            
        if found == False:
            print("Invalid pokemon")
        print(self.pokemon_names[self.currently_active] + " I choose you!")

    # Method for a battle round
    def battle_round(self, opponent):
        choice_made = False
        while choice_made == False:
            print("Press 'a' to attack, press 'b' to use a potion")
            choice = input()
            if choice == "a":
                self.trainer_attack(opponent)
                opponent.trainer_attack(self)
                choice_made = True
            elif choice == "b":
                self.use_potion()
                opponent.trainer_attack(self)
                choice_made = True
            else:
                print("Invalid input")

    # Method for a battle
    def battle(self, opponent):
        print(opponent.name + " challenges you to a battle!")
        print(opponent.name + " sends out " + opponent.pokemon[opponent.currently_active].name + "!")
        print(self.name + ": Go " + self.pokemon[self.currently_active].name)
        battling = True
        while battling == True:
            self.count = 0
            opponent.count = 0
            for trainer in [self, opponent]:
                for i in range(len(trainer.pokemon)):
                    if trainer.pokemon[i].knocked_out == True:
                        trainer.count += 1
            if self.count == len(self.pokemon):
                print(self.name + "is out of useable Pokemon. You loose!")
                battling = False
            elif opponent.count == len(opponent.pokemon):
                print(opponent.name + "is out of useable Pokemon. You win!")
                battling = False
            else:
                self.battle_round(opponent)


    