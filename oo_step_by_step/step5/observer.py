class KlassPublisher:
    def register(self, observer):
        pass

    def unregister(self, observer):
        pass


class KlassInfo:
    def __init__(self, name, klass_number, is_leader):
        self.name = name
        self.klass_number = klass_number
        self.is_leader = is_leader


class KlassObserver:
    def update(self, student_info: KlassInfo):
        pass
