# CLASS LIST: GROSPE
from pyscript import display, document

classmates = []

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return self.name + " is from " + self.section + " and likes " + self.favorite_subject + "."

classmates.append(Classmate("Aseo", "Sapphire", "Science"))
classmates.append(Classmate("Batac", "Sapphire", "English"))
classmates.append(Classmate("Calanglang", "Sapphire", "Social Studies"))
classmates.append(Classmate("Dee", "Sapphire", "Science"))
classmates.append(Classmate("De Guzman", "Sapphire", "Math"))

def information(e):
    document.getElementById("output").innerHTML = ""

    for x in classmates:
        display(x.introduce(), target="output")

def insert_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    for x in classmates:
        if x.name == name and x.section == section and x.favorite_subject == subject:
            display("This classmate is already in the list.", target="output")
            return

    new_classmate = Classmate(name, section, subject)
    classmates.append(new_classmate)

    display("New classmate added!", target="output")