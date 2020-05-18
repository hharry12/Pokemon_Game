import sys 

sys.path.insert(1, '../model')

from tkinter import *
import GUI


class Game:
    #if __name__ == "__main__":

        def __init__(self):
            self.initialiseGame()
            self.runGame()
            self.endGame()


        def initialiseGame(self):
           root = Tk()
           pokemon = GUI.Window(root)
           root.mainloop()
        
            

            
        def runGame(self):
            pass
            #start the game loop
            #run = True
            #while run == True:
                
              #  run = False
                
                
        

        def endGame(self):
            #clean up any data etc when the game ends
            #print("No code in end game method")
            pass
        
            

Pokemon = Game()
