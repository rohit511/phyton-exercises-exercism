
class School:
    def __init__(self):
        self.dictie = {}        # dict containing grades as keys and lists of students in a grade as their values.
        self.expectation = []   # it asks to return True in list as many times as students are added. Did so.
    def add_student(self, name, grade):
        for v in self.dictie.values():  # if name already in any grade
            if name in v:
                self.expectation.append(False)
                return None
            
        if grade in self.dictie:        # if grade exists in dict.keys, append name
            self.dictie[grade].append(name) #Self.dictie[grade].append(name)
        else:                           # else, create grade then append
            self.dictie[grade] = [name]
        self.expectation.append(True) 
    
    def roster(self):                   # create sorted roster/scoreboard, in which names in a grade are sorted alphabetically and names are in order of increasing grade.
        roster, grades = [], [] 
        for k in self.dictie: 
            grades.append(k)
        grades.sort()
        for k in grades:
            temp_list = self.dictie[k]
            temp_list.sort() 
            roster.extend(temp_list)
        return roster 
    def grade(self, grade_number):        # gives sorted list of names in a grade
        try: 
            students = self.dictie[grade_number] #
        except KeyError:
            students = [] 
        else:
            students.sort()
        return students 
    def added(self):                      # tell how manay students have been added.
        return self.expectation