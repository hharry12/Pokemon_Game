import sys 

sys.path.insert(1, '../model')

from tkinter import *
import GUI


class Game:
    if __name__ == "__main__":

        def __init__(self):
            self.run_game()
            self.end_game()


        def run_game(self):
           root = Tk()
           pokemon = GUI.Window(root)
           root.mainloop()
    

        def end_game(self):
            # Method not needed yet
            pass
        
            

Pokemon = Game()
