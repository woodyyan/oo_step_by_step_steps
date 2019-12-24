
class Person:
    def __init__(self, id, name, age) -> None:
        self.id = id
        self.name = name
        self.age = age

    def introduce(self):
        return "My name is " + self.name + ". I am " + \
               str(self.age) + " years old."
        
        
