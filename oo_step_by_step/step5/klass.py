from oo_step_by_step.step5.observer import Subject


class Klass(Subject):
    def __init__(self, klass_number) -> None:
        self.klass_number = klass_number
        self.leader = None
        self.__observers = []

    def __str__(self) -> str:
        if self.klass_number <= 0:
            return "No Class"
        return "Class {self.klass_number}".format(self=self)

    def eqauls(self, otherKlass) -> bool:
        return self.klass_number == otherKlass.klass_number

    def assign_leader(self, leader):
        if leader.in_klass(self):
            self.leader = leader
        else:
            print("It's not one of us.")

    def has_leader(self, leader):
        return self.leader is not None and self.leader.equals(leader)

    def append_member(self, student):
        student.resign_to(self)

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observber):
        self.__observers.remove(observber)

    def notify(self):
        for observer in self.__observers:
            observer.update(self)

