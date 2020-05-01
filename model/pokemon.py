class Pokemon:

    def __init__(self, name, level, type, knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = 10 + (2*level)
        self.current_health = self.maximum_health
        self.knocked_out = knocked_out
        self.remaining_xp = level*50
    

    # Method for loosing health
    def lose_health(self, damage):

        # Take away health
        if (self.current_health - damage) > 0:
            print(self.name + " lost " + str(damage) + " health!")
            self.current_health -= damage
        
        # Edge case where Pokemon runs out of health
        else:
            print("Oh no! " + self.name + " fainted!")
            self.current_health = 0
            self.knocked_out = True

    

    # Method for regaining health
    def gain_health(self, health):

        # Add health
        if (self.current_health + health) < self.maximum_health:
            print(self.name + " gains " + str(health) + " health!")
            self.current_health += health

        # Edge case where pokemon already has full health
        elif self.current_health == self.maximum_health:
            print(self.name + " is already at full health.")

        # Edge case where pokemon regains full health
        else:
            print(self.name + " is back to full health!")
            self.current_health = self.maximum_health
        
    # Method for reviving a Pokemon
    def revive(self):
        if self.knocked_out == True:
            self.current_health += self.maximum_health/2
            self.knocked_out = False
            print(self.name + " is no longer knocked out. " + self.name + " is now at " + str(self.current_health) + " health.")
        else:
            print("Cannot use revive on " + self.name + ".")


    # Method for attacking a Pokemon, includes experience and levelling system with if loops.
    def attack(self, victim):

        if self.knocked_out == False:

            # Determine type difference - atm only works for fire grass and water
            print(self.name + " attacks " + victim.name + ".")
            if (self.type == "water" and victim.type == "fire") or (self.type == "fire" and victim.type == "grass") or (self.type == "grass" and victim.type == "water"):
             multiplier = 2
            else:
             multiplier = 0.5 
            damage = self.level*multiplier
            #call lose_health method
            victim.lose_health(damage)

            # If attacked pokemon is knowxked out, we need to gain xp.
            if victim.knocked_out == True:
                if self.level == 100:
                    print(self.name + " has reached max level 100 and cannot gain experience points.")
                else:
                    xp = victim.level*5
                    print(self.name + " gained " + str(xp) + " experience points!")

                    # If pokemon gains enough xp it needs to level up
                    if self.remaining_xp <= xp:
                        self.level += 1
                        self.remaining_xp = self.level*50
                        print(self.name + " levelled up to level " + str(self.level) + "!")
                    else:
                        self.remaining_xp -= xp
        else:
            print(self.name + " is knocked out, it cannot attack.")