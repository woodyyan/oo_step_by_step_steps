from oo_step_by_step.step5.klass import Klass
from oo_step_by_step.step5.observer import KlassObserver, KlassInfo


class X(KlassObserver):
    def __init__(self, klass: Klass):
        self.klass = klass

    def update(self, klass_info: KlassInfo):
        if klass_info.klass_number == self.klass.klass_number:
            if klass_info.is_leader:
                print('I am the Machine. I know %s become Leader of Class %s.' % (
                    klass_info.name, klass_info.klass_number))
            else:
                print(
                    'I am the Machine. I know %s has joined Class %s.' % (klass_info.name, klass_info.klass_number))
