import random
class Time_answer:
    def __init__(self):
        self.defaultAnswers = []
        self.defaultAnswers.append("Still here? I thought I said something wrong..")
        self.defaultAnswers.append("What's wrong?")
        self.defaultAnswers.append("Hey, where have you been?")
        self.defaultAnswers.append("I hope it's everything ok.")
        self.defaultAnswers.append("Hey, smile! Life is too short to be mad :)")

    def time_answer(self, time):
        if time >= 60:
            rnd = random.randint(1, 100)
            return defaultAnswer[rnd]

