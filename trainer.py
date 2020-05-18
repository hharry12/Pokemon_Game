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
    def use_potion(self, pokemon):
        if self.potions != 0:
            result = self.name + " used a potion. "
            result += pokemon.gain_health(20)
            self.potions -= 1
            return result
        else:
            return self.name + " has no potions remaining. "
    
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
        result = self.pokemon[self.currently_active].attack(trainer.pokemon[trainer.currently_active])
        return result

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
    

    # Method for a battle
    def battle_init(self, opponent):
        return opponent.name + " challenges you to a battle! " + opponent.name + " sends out " + opponent.pokemon[opponent.currently_active].name + "!"

    

    def battle_round(self, choice, opponent):

            result = ""
            if choice == 1:
                string1 = self.trainer_attack(opponent)
                result += string1
                string2 = opponent.trainer_attack(self)
                result += string2
                self.count = 0
                opponent.count = 0
                for trainer in [self, opponent]:
                    for i in range(len(trainer.pokemon)):
                        if trainer.pokemon[i].knocked_out == True:
                            trainer.count += 1
                if self.count == len(self.pokemon):
                    result += self.name + "is out of useable Pokemon. You loose!"
                    scenario = 2
                elif opponent.count == len(opponent.pokemon):
                    result += opponent.name + "is out of useable Pokemon. You win!"
                    scenario = 2
                else:
                    scenario = 1
                return [result, scenario]
            elif choice == 2:
                # Below only works on first pokemon in list NEEDS UPDATING
                result = self.use_potion(self.pokemon[0])
                result += opponent.trainer_attack(self)
                scenario = 1
                
                return [result, scenario]
    


        