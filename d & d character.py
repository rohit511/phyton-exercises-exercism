import random
abilities =["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
def modifier(score):
    return (score - 10) // 2
class Character:
    def __init__(self):
        for a in abilities:
            setattr(self, a, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)
    
    def ability(self):
        score = sorted(random.randint(1,6) for i in range(4))
        return sum(score[1:])     