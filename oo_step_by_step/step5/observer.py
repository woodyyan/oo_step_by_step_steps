class Publisher:
    def register(self, observber):
        pass

    def unregister(self, observber):
        pass

    def notify(self):
        pass


class StudentInfo:
    def __init__(self, name, klass_number):
        self.name = name
        self.klass_number = klass_number


class Observer:
    def update(self, student_info: StudentInfo):
        pass
