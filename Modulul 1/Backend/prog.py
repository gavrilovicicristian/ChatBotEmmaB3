from flask import Flask
from flask_cors import CORS, cross_origin
import MySQLdb, aiml,os,json
from memory_check import Memory
import threading
from mood import Mood
from personBD import *
from personality import *
from randomAnswer import RandomAnswer
import random
import isEnglishOrJibberish
app = Flask(__name__)

db = MySQLdb.connect(host="ppdatabase.ccvycmsqlp8u.eu-central-1.rds.amazonaws.com",    # your host, usually localhost
                     user="mariusdonici",         # your username
                     passwd="carrymeteodorescu",  # your password
                     db="ia")        # name of the data base

cur = db.cursor()

# Use all the SQL you like

# for row in cur.fetchall():
#     print row[0]
cur.execute("SELECT * FROM persons")

table= cur.fetchall()
cur.execute("SELECT * FROM questions")
questions = cur.fetchall()
db.close()

rnd = RandomAnswer()
sessionId=12345
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

initialize_bot(kernel,sessionId)

botMood = Mood()

attr=getPeopleAttributes()
iKnowOp=2
pairQA_dict={}
res=""
# Press CTRL-C to break this loop
sendNew_res=0
#load json
json_data=open("QA.json").read()
all_QA=json.loads(json_data)
@app.route('/<question>')
def main(question):
    global attr
    global iKnowOp
    global pairQA_dict
    global res
    global sendNew_res
    print botMood.get_current_mood(question)
    #users=table
    bootMemory= Memory()
    if not sendNew_res and res.endswith('?'):
        if len(attr)==1:
            pers=attr[0]
            print res
            print all_QA[str(pers[0])].keys()
            if res in all_QA[str(pers[0])].keys():
                aux_d=all_QA[str(pers[0])]
                if aux_d[res].lower()!=question.lower():
                    # print aux_d[res]
                    new_res= "But last time you said other thing. I quote: " +str(aux_d[res])
                    aux_d[res]=question
                    sendNew_res=1
                    return new_res
        pairQA_dict[res]=question
    sendNew_res=0
    res=kernel.respond(question,sessionId)
    if res=='CLOSING SESSION':
        print pairQA_dict
        if len(attr)==1:
            pers = attr[0]
            # memorate_QA(pers[0],pairQA_dict)
            if pairQA_dict is not None:
                if str(pers[0]) in all_QA:
                    all_QA[str(pers[0])].update(pairQA_dict)
                else:
                    all_QA[pers[0]]=pairQA_dict
                twitterDataFile = open("QA.json", "w")
                # magic happens here to make it pretty-printed
                twitterDataFile.write(json.dumps(all_QA, indent=4, sort_keys=True))
                twitterDataFile.close()
        elif len(attr)==0:
            memoratePerson(kernel,sessionId)
        exit(1)

    responses_incase_nonenglish = open('jibberish_responses.json', 'r').read()
    jibberish_array = json.loads(responses_incase_nonenglish)
    if not (isEnglishOrJibberish.is_english_sentence(question)):
        return random.choice(jibberish_array)
    res=synonymCheck("resources/synonyms.json",question)
    if bootMemory.checkQuestionRepetition(question)==1:
        bootMemory.addQuestion(question)
        response=bootMemory.getRandomForRepetition()
        bootMemory.addResponse(response)
        return response
    bootMemory.addQuestion(question)

    if len(attr)>1:
        attr=verifyExistence(kernel,sessionId,attr)
    if len(attr)==1:
        iKnowOp=1
        pers=attr[0]
        updateAttributes(kernel,attr[0],sessionId)
    if len(attr)==0:
        iKnowOp=0
        decideToMemorate(kernel,sessionId)
    if res=='':
        res = rnd.answer(questions)

    bootMemory.addResponse(res)

    return res


def deleteContent(fName):
    with open(fName, "w"):
        pass


def synonymCheck(filePath, question):
    res=kernel.respond(question,sessionId)
    if res is not None:
        return res
    with open(filePath) as data_file:
        data = json.load(data_file)
    for i in data:
        aux = question
        for j in data[i]:
            aux = aux.replace(i, data[i][j])
            res=kernel.respond(aux,sessionId)
            if res is not None:
                return res
            aux = question
    return "No answer found"


if __name__ == '__main__':
    CORS(app)
    deleteContent('question.txt')
    app.run();