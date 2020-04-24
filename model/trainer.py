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
            self.pokemon.append(Pokemon(self.name + "s' " + pokemon[i], levels[i], types[i], False))

    # Method for using potions
    def use_potion(self, pokemon):
        print(self.name + " used a potion")
        found = False
        for i in range(len(self.pokemon)):
            if self.pokemon[i].name == self.name + "s' " + str(pokemon):
                self.pokemon[i].gain_health(20)
                found = True
        if found == False:
            print("Invalid pokemon")
    

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
