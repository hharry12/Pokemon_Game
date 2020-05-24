from tkinter import *
import trainer as tr
from functools import partial


class Window(Canvas):
    
    def __init__(self, master):
        super().__init__(
            width=600, height=620, background="white", highlightthickness=0
        )
     
        self.master = master

        # Create text label, output for the game narrative.
        self.text = StringVar()
        self.text.set("""Professor: Hello and welcome to the world of pokemon. 
        I am the mandatory Professor! What is your name?""")
        self.label = Label(self.master, textvariable = self.text)
        self.label.pack()

        # Create Button text variables
        self.button1_text = StringVar()
        self.button1_text.set("Red")
        self.button2_text = StringVar()
        self.button2_text.set("Blue")
        self.button3_text = StringVar()
        self.button3_text.set("Bulbasaur")
        self.buttons_func(2,0)

        # Below variable is made so that the code knows how far through the game the user is.
        self.scenario = StringVar()
        self.scenario.set("Initialise")

    # Method to change number of buttons in GUI, destroys old and makes new everytime, this could
    # perhaps be done better
    def buttons_func(self, create, destroy):

        # First destory old buttons, depending on how many there are
        if destroy == 1:
            self.button1.destroy()

        elif destroy == 2:
            self.button1.destroy()
            self.button2.destroy()

        elif destroy == 3:
            self.button1.destroy()
            self.button2.destroy()
            self.button3.destroy()
        
        
        # Next create new buttons, again depending on how many we need.
        if create == 1:
            self.button1 = Button(self.master, textvariable = self.button1_text, 
            command = partial(self.next_action, 1))
            self.button1.pack()

        elif create == 2:
            
            self.button1 = Button(self.master, textvariable = self.button1_text, 
            command = partial(self.next_action, 1))                
            self.button1.pack()

            self.button2 = Button(self.master, textvariable = self.button2_text, 
            command = partial(self.next_action, 2))
            self.button2.pack()

        elif create == 3:
            print(self.button1_text.get())
            self.button1 = Button(self.master, textvariable = self.button1_text, 
            command = partial(self.next_action, 1))
            self.button1.pack()

            self.button2 = Button(self.master, textvariable = self.button2_text, 
            command = partial(self.next_action, 2))
            self.button2.pack()

            self.button3 = Button(self.master, textvariable = self.button3_text, 
            command = partial(self.next_action, 3))
            self.button3.pack()
        else:
            pass

    # Method to decide which functions to call, depending how far through the game the user is.    
    def next_action(self, button_no):

        scenario = self.scenario.get()

        if scenario == "Initialise":
            self.get_name(button_no)
            self.scenario.set("Initialise2")
            self.buttons_func(3,2)
            self.button1_text.set("Charmander")
            self.button2_text.set("Squirtle")

        elif scenario == "Initialise2":
            self.get_choice(button_no)
            self.player = tr.Trainer(self.name, [self.starter_choice], [5], 
            [self.starter_type], 1, 0)
            self.professor = tr.Trainer("Professor", [self.professor_starter], [5], 
            [self.professor_type], 0, 0)
            self.scenario.set("Battle")
            self.buttons_func(1,3)
            self.button1_text.set("Start battle")

        elif scenario == "Battle":
            self.text.set(self.player.battle_init(self.professor))
            self.scenario.set("Battle choice")
            self.buttons_func(2,1)
            self.button1_text.set("Attack")
            self.button2_text.set("Use Potion")

        elif scenario == "Battle choice":
            result = self.player.battle_round(button_no, self.professor)
            self.text.set(result[0])
            if result[1] == 2:
                self.scenario.set("End")
                self.buttons_func(1,2)
                self.button1_text.set("Thanks for playing")
            

        elif scenario == "End":
            self.master.destroy()


    
    # Next two methods are used to get parameters to create a trainer instance for the player.
    # The class which all future functions are called.
    # ****NEEDS UPDATE**** - Cannot input actual name, just uses default Red or Blue
    def get_name(self, button_no):
        if button_no == 1:
            self.name = "Red"
        elif button_no == 2:
            self.name = "Blue"
        self.change_text("Professor: " + self.name + """ Great name! 
        I have three pokemon for you to choose from. 
        Charmander the fire type, Squirtle the water type or Bulbasaur the grass type!""")

    def get_choice(self, button_no):
        
        if button_no == 1:
            self.starter_choice = "Charmander"
            self.starter_type = "fire"
            self.professor_starter = "Bulbasaur"
            self.professor_type = "grass"

        elif button_no == 2:
            self.starter_choice = "Squirtle"
            self.starter_type = "water"
            self.professor_starter = "Charmander"
            self.professor_type = "fire"

        elif button_no == 3:
            self.starter_choice = "Bulbasaur"
            self.starter_type = "grass"
            self.professor_starter = "Squirtle"
            self.professor_type = "water"

        self.change_text("Professor: Ah, a " + self.starter_choice + """! Good choice! 
        Professor: Now I shall randomly battle you as that's all that's been coded into this game so far!""")


    def change_text(self, text):    
        self.text.set(text)
