from oo_step_by_step.step3.person import Person


class Worker(Person):


    def introduce(self):
        return super().introduce() + " I am a Worker. I have a job."


