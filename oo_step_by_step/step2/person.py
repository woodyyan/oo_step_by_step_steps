
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def introduce(self):
        return "My name is " + self.name + ". I am " + \
               str(self.age) + " years old."
        
        
