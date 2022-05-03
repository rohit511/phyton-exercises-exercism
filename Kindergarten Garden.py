plant_types = {
    "R": "Radishes",
    "C": "Clover",
    "G": "Grass",
    "V": "Violets"
}
class Garden:
    all_students = ["Alice", "Bob", "Charlie", "David",
                    "Eve", "Fred", "Ginny", "Harriet",
                    "Ileana", "Joseph", "Kincaid", "Larry"]
    
    def __init__(self, diagram = "", students = all_students):
        self.students = sorted(students)
        self.diagram = diagram.split("\n")
        pass
    def plants(self, name):
        start_pt = self.students.index(name) * 2
        lst = []
        for row in self.diagram:
            for p in row[start_pt : start_pt + 2]:
                lst.append(plant_types[p])
        return lst