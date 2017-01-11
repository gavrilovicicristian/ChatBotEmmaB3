import random

class RandomAnswer:
    def __init__(self):
        self.defaultAnswers = []
        self.defaultAnswers.append("Still here?")
        self.defaultAnswers.append("What's wrong?")
        self.defaultAnswers.append("Hey, where are you?")
        self.defaultAnswers.append("Tell me something..")
        self.defaultAnswers.append("Hey, smile! Life is too short to be mad :)")

    def answer(self, questions):
        rnd = random.randint(1,100)
        question = "Random question."
        print("Probability for random question: %d" % rnd)
        if rnd <= 45:
            length = len(questions)
            if length!=0:
                randId = random.randint(1, length)
                print("randId: %d" % randId)
                question = questions[randId-1][1]
        else:
            number = random.randint(0,4)
            question = self.defaultAnswers[number]
        print("Question: %s" %question)
        return question
