from tkinter import *
import trainer as tr
from functools import partial
from PIL import Image
from PIL import ImageTk


class Window(Canvas):
    
    def __init__(self, master):
        super().__init__(
            width=1000, height=1000, background="white", highlightthickness=0
        )
        
        self.master = master

        # Below variable is made so that the code knows how far through the game the user is.
        self.scenario = StringVar()
        self.scenario.set("Initialise")
        
        # Create text label, output for the game narrative.
        self.text1 = StringVar()
        self.text1.set("""Professor: Hello and welcome to the world of pokemon. 
        I am the mandatory Professor! What is your name?""")
        self.text2 = StringVar()
        self.text2.set("")
        self.text3 = StringVar()
        self.text3.set("")
        self.labelim1 = StringVar()
        self.labelim1.set("pic.png")
        self.labelim2 = StringVar()
        self.labelim2.set("blank.png")
        self.labelim3 = StringVar()
        self.labelim3.set("blank.png")
        self.labels_func(1,0)

        # Create Button text variables
        self.button1_text = StringVar()
        self.button1_text.set("Red")
        self.button2_text = StringVar()
        self.button2_text.set("Blue")
        self.button3_text = StringVar()
        self.button3_text.set("Bulbasaur")
        self.buttonim1 = StringVar()
        self.buttonim1.set('blank.png')
        self.buttonim2 = StringVar()
        self.buttonim2.set('blank.png')
        self.buttonim3 = StringVar()
        self.buttonim3.set('blank.png')
        self.buttons_func(2,0)

        

    def labels_func(self, create, destroy):
        
        if destroy == 0:
            pass
        elif destroy == 1:
            self.label1.destroy()

        elif destroy == 2:
            self.label1.destroy()
            self.label2.destroy()


        if create == 1:
            image_name1 = self.labelim1.get()
            label_image1 = Image.open(image_name1)
            self.label_photo1 = ImageTk.PhotoImage(label_image1)
            
            self.label1 = Label(self.master, textvariable = self.text1, image = self.label_photo1, compound = TOP)
            #self.label1.photo = self.photo
            self.label1.pack()

        elif create == 2:
            image_name1 = self.labelim1.get()
            label_image1 = Image.open(image_name1)
            self.label_photo1 = ImageTk.PhotoImage(label_image1)
            
            image_name2 = self.labelim2.get()
            label_image2 = Image.open(image_name2)
            self.label_photo2 = ImageTk.PhotoImage(label_image2)

            self.label1 = Label(self.master, textvariable = self.text1, image = self.label_photo1, compound = TOP)
            #self.label1.photo = self.photo
            self.label1.pack()

            self.label2 = Label(self.master, textvariable = self.text2, image = self.label_photo2, compound = TOP)
            #self.label2.photo = self.photo
            self.label2.pack()

        elif create == 3:
            
            image_name1 = self.labelim1.get()
            label_image1 = Image.open(image_name1)
            self.label_photo1 = ImageTk.PhotoImage(label_image1)
            
            image_name2 = self.labelim2.get()
            label_image2 = Image.open(image_name2)
            self.label_photo2 = ImageTk.PhotoImage(label_image2)

            image_name3 = self.labelim3.get()
            label_image3 = Image.open(image_name3)
            self.label_photo3 = ImageTk.PhotoImage(label_image3)
            
            self.label1 = Label(self.master, textvariable = self.text1, image = self.label_photo1, compound = TOP)
            #self.label1.photo = self.photo
            self.label1.pack()

            self.label2 = Label(self.master, textvariable = self.text2, image = self.label_photo2, compound = TOP)
            #self.label2.photo = self.photo
            self.label2.pack(side = LEFT)

            self.label3 = Label(self.master, textvariable = self.text3, image = self.label_photo3, compound = TOP)
            #self.label3.photo = self.photo
            self.label3.pack(side = RIGHT)



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

            buttonim1 = self.buttonim1.get()
            button_image1 = Image.open(buttonim1)
            self.photo1 = ImageTk.PhotoImage(button_image1)

            self.button1 = Button(self.master, textvariable = self.button1_text, 
            command = partial(self.next_action, 1), image = self.photo1, compound = TOP)
            self.button1.pack()

        elif create == 2:
            

            buttonim1 = self.buttonim1.get()
            button_image1 = Image.open(buttonim1)
            self.photo1 = ImageTk.PhotoImage(button_image1)

            buttonim2 = self.buttonim2.get()
            button_image2 = Image.open(buttonim2)
            self.photo2 = ImageTk.PhotoImage(button_image2)
            
            self.button1 = Button(self.master, textvariable = self.button1_text, image = self.photo1, 
            compound = TOP, command = partial(self.next_action, 1))
            self.button1.pack()
        
            self.button2 = Button(self.master, textvariable = self.button2_text, image = self.photo2, 
            compound = TOP, command = partial(self.next_action, 2))
            self.button2.pack()

        elif create == 3:

            buttonim1 = self.buttonim1.get()
            button_image1 = Image.open(buttonim1)
            self.photo1 = ImageTk.PhotoImage(button_image1)

            buttonim2 = self.buttonim2.get()
            button_image2 = Image.open(buttonim2)
            self.photo2 = ImageTk.PhotoImage(button_image2)

            buttonim3 = self.buttonim3.get()
            button_image3 = Image.open(buttonim3)
            self.photo3 = ImageTk.PhotoImage(button_image3)

            self.button1 = Button(self.master, textvariable = self.button1_text, image = self.photo1,
            command = partial(self.next_action, 1), compound = TOP)
            self.button1.pack(side = LEFT)

            self.button2 = Button(self.master, textvariable = self.button2_text, 
            command = partial(self.next_action, 2), image = self.photo2, compound = TOP)
            self.button2.pack()

            self.button3 = Button(self.master, textvariable = self.button3_text, 
            command = partial(self.next_action, 3), image = self.photo3, compound = TOP)
            self.button3.pack(side = RIGHT)
        else:
            pass

    # Method to decide which functions to call, depending how far through the game the user is.    
    def next_action(self, button_no):
        
        scenario = self.scenario.get()

        if scenario == "Initialise":
            self.get_name(button_no)
            self.scenario.set("Initialise2")
            self.buttons_func(1,2)
            self.button1_text.set("Show me!")
                    

        elif scenario == "Initialise2":
            self.labelim1.set('blank.png')
            self.labels_func(1,1)
            #image = Image.open('blank.png')
            
            self.change_text("Choose from the following!")

            self.buttonim1.set('Charmander.png')
            self.buttonim2.set('Squirtle.png')
            self.buttonim3.set('Bulbasaur.png')
            
            self.buttons_func(3,2)
            self.button1_text.set("Charmander")
            self.button2_text.set("Squirtle")
            
            self.scenario.set("Initialise3")

        elif scenario == "Initialise3":
            self.get_choice(button_no)
            self.player = tr.Trainer(self.name, [self.starter_choice], [5], 
            [self.starter_type], 1, 0)
            self.professor = tr.Trainer("Professor", [self.professor_starter], [5], 
            [self.professor_type], 0, 0)
            self.scenario.set("Battle")
            if button_no == 1:
                self.buttonim1.set('Charmander.png')
            elif button_no == 2:
                self.buttonim1.set('Squirtle.png')
            elif button_no == 3:
                self.buttonim1.set('Bulbasaur.png')
            self.buttons_func(1,3)
            self.button1_text.set("Start battle")

        elif scenario == "Battle":
            
            self.text1.set(self.player.battle_init(self.professor))
            self.text2.set(self.player.name + "'s " + self.starter_choice + ": " + str(self.player.pokemon[self.player.currently_active].current_health))
            self.text3.set("Professor's " + self.professor_starter + ": " + str(self.professor.pokemon[self.professor.currently_active].current_health))
            self.labelim1.set('blank.png')
            if self.starter_choice == "Charmander":
                self.labelim2.set('Charmander.png')
                self.labelim3.set('Bulbasaur.png')
            elif self.starter_choice == "Squirtle":
                self.labelim2.set('Squirtle.png')
                self.labelim3.set('Charmander.png')
            elif self.starter_choice == "Bulbasaur":
                self.labelim2.set('Bulbasaur.png')
                self.labelim3.set('Squirtle.png')
            self.labels_func(3,1)
            self.scenario.set("Battle choice")
            self.buttonim1.set('blank.png')
            self.buttonim2.set('blank.png')
            self.buttons_func(2,1)
            self.button1_text.set("Attack")
            self.button2_text.set("Use Potion")
            


        elif scenario == "Battle choice":
            result = self.player.battle_round(button_no, self.professor)
            self.text1.set(result[0])
            self.text2.set(self.player.name + "'s " + self.starter_choice + ": " + str(self.player.pokemon[self.player.currently_active].current_health))
            self.text3.set("Professor's " + self.professor_starter + ": " + str(self.professor.pokemon[self.professor.currently_active].current_health))
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
        I have three pokemon for you to choose from.""")

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
        Professor: A pokemon trainer must always be ready for battle, face me!""")


    def change_text(self, text):    
        self.text1.set(text)
