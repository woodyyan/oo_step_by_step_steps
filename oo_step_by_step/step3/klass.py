

class Klass:
    def __init__(self, klass_number) -> None:
        self.klass_number = klass_number
        self.leader = None

    def __str__(self) -> str:
        if self.klass_number <= 0:
            return "No Class"
        return "Class {self.klass_number}".format(self = self)

    def eqauls(self, otherKlass) -> bool:
        return self.klass_number == otherKlass.klass_number

    def assign_leader(self, leader):
        self.leader = leader

    def has_leader(self, leader):
        return self.leader is not None and self.leader.equals(leader)
