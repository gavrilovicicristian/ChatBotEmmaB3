import random


class Memory:
    responseList=[]
    def __init__(self):
        self.responseList.append('You said that.')
        self.responseList.append('You already said that.')
        self.responseList.append('Why do you tell me this again?')
        self.responseList.append('I know, you said that...')
        self.responseList.append('Not again *eyes rolling*')
        self.responseList.append('Really?')



    def getRandomForRepetition(self):
        return self.responseList[random.randint(0,5)]

    def addResponse(self,response):
        try:
            theFile = open('question.txt', 'a')
            theFile.write("[Response]" + response + "\n")
        except ValueError:
            print('Eroare la scriere raspuns')

    def addQuestion(self,question):
        try:
            theFile = open('question.txt', 'a')
            theFile.write("[Question]" + question + "\n")
        except ValueError:
            print("Eroare la scriere intrebare")

    def checkQuestionRepetition(self,question):
        try:
            with open('question.txt', 'r') as theFile:
                lines = theFile.readlines()
                for i in lines:
                    if i == '[Question]' + question + '\n':
                        return 1

        except ValueError:
            print('Eroare la scriere raspuns')
