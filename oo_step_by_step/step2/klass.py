
class Klass:
    def __init__(self, klass_number) -> None:
        self.klass_number = klass_number

    def __str__(self) -> str:
        if self.klass_number <= 0:
            return "No Class"
        return "Class {self.klass_number}".format(self = self)

        