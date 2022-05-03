class Allergies:
    allergenes ={1:'eggs', 2:'peanuts', 4:'shellfish',8:'strawberries',16:'tomatoes',32:'chocolate', 64:'pollen', 128: 'cats'}
    score_sub = [1,2,4,8,16,32,64,128]
    all_allergenes =[]
    def __init__(self, score):
        self.score = score
    def allergic_to(self, item):
        self.all_allergenes = []
        i = -1
        while self.score > 0:
            if self.score_sub[i] <= self.score:
                self.score-=self.score_sub[i]
                self.all_allergenes.append(self.allergenes[self.score_sub[i]])
            else:
                i-=1
        if item in self.all_allergenes:
            return True
        else:
            return False
            
    @property
    def lst(self):
        self.all_allergenes = []
        i = -1
        while self.score > 0:
            if self.score_sub[i] <= self.score:
                self.score-=self.score_sub[i]
                self.all_allergenes.append(self.allergenes[self.score_sub[i]])
            else:
                i-=1
        return list(dict.fromkeys(self.all_allergenes))