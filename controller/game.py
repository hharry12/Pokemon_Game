import sys 

sys.path.insert(1, '../model')

import trainer as trainermod

class Game:
    if __name__ == "__main__":
    
        

        def initialiseGame(self):
            pass

            
        def runGame(self):
            #start the game loop
            run = True
            while run == True:
                #initialise game introdution
                print("Professor: Hello and welcome to the world of pokemon, I am the mandatory Professor! What is your name?")
                name = input()
                # Get player to choose their starting Pokemon. Then instatiate a trainer object for the player and 'Proffesor'
                print("Professor: " + name + "! Great name! I have three pokemon for you to choose from. Type 'a' for a Charmander, 'b' for a Squirtle or 'c' for a Bulbasaur!")
                choice_made = False
                while choice_made == False:
                    pokemon_choice = input()
                    if pokemon_choice == "a":
                        pokemon_choice = "Charmander"
                        pokemon_type = "fire"
                        choice_made = True
                        professor = trainermod.Trainer("Professor", ["Bulbasaur"], [5], ["grass"], 0, 0)
                    elif pokemon_choice == "b":
                        pokemon_choice = "Squirtle"
                        pokemon_type = "water"
                        choice_made = True
                        professor = trainermod.Trainer("Professor", ["Charmander"], [5], ["fire"], 0, 0)
                    elif pokemon_choice == "c":
                        pokemon_choice = "Bulbasaur"
                        pokemon_type = "grass"
                        choice_made = True
                        professor = trainermod.Trainer("Professor", ["Squirtle"], [5], ["water"], 0, 0)
                    else:
                        print("I'm sorry that's not a valid input, type 'a' for a Charmander, 'b' for a Squirtle or 'c' for a Bulbasaur.")
                trainer = trainermod.Trainer(name, [pokemon_choice], [5], [pokemon_type], 1, 0)
                print("Professor: Ah, a " + pokemon_choice + "! Good choice!")
                print("Professor: Now I shall randomly battle you as that's all that's been coded into this game so far!")
                
                # Start battle
                trainer.battle(professor)

                print("Thanks for playing the game!")
                run = False
                
                
        

        def endGame(self):
            #clean up any data etc when the game ends
            #print("No code in end game method")
            pass

        def __init__(self):
            self.initialiseGame()
            self.runGame()
            self.endGame()
            

Pokemon = Game()
