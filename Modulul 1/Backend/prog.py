from flask import Flask
from flask_cors import CORS, cross_origin
import MySQLdb, aiml,os
from memory_check import Memory
import threading
app = Flask(__name__)

db = MySQLdb.connect(host="ppdatabase.ccvycmsqlp8u.eu-central-1.rds.amazonaws.com",    # your host, usually localhost
                     user="mariusdonici",         # your username
                     passwd="carrymeteodorescu",  # your password
                     db="ia")        # name of the data base

cur = db.cursor()

# Use all the SQL you like

# for row in cur.fetchall():
#     print row[0]
cur.execute("SELECT * FROM Users")

table= cur.fetchall()

sessionId=12345
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# # kernel.setPredicate("dog", "Brandy", sessionId)
# kernel.setPredicate("name", "Alexa Vasilovici", sessionId)
# # kernel.setPredicate("age", "25", sessionId)

# Press CTRL-C to break this loop
@app.route('/<question>')
def main(question):
    users=table
    bootMemory= Memory()
    res=kernel.respond(question,sessionId)
    if bootMemory.checkQuestionRepetition(question)==1:
        bootMemory.addQuestion(question)
        response=bootMemory.getRandomForRepetition()
        bootMemory.addResponse(response)
        return response
    bootMemory.addQuestion(question)
    bootMemory.addResponse(res)
    name=kernel.getPredicate("name",sessionId)
    dog = kernel.getPredicate("dog", sessionId)
    if name!="":
        users=[t for t in users if t[1]==name]
    if dog!="":
        users=[t for t in users if t[4]==dog]
    if len(users)==1:
        user=users[0]
        kernel.setPredicate("lastname",user[2],sessionId)
    if res=='':
        return 'I do not know the answer to that.'
    return res
db.close()

def deleteContent(fName):
    with open(fName, "w"):
        pass

if __name__ == '__main__':
    CORS(app)
    deleteContent('question.txt')
    app.run();