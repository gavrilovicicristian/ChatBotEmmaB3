from flask import Flask
from flask_cors import CORS, cross_origin
import MySQLdb, aiml,os



app = Flask(__name__)

db = MySQLdb.connect(host="ppdatabase.ccvycmsqlp8u.eu-central-1.rds.amazonaws.com",    # your host, usually localhost
                     user="mariusdonici",         # your username
                     passwd="chatbot",  # your password
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
def lel(question):
    users=table

    res=kernel.respond(question,sessionId)
    name=kernel.getPredicate("name",sessionId)
    dog = kernel.getPredicate("dog", sessionId)
    if name!="":
        users=[t for t in users if t[1]==name]
    if dog!="":
        users=[t for t in users if t[4]==dog]
    if len(users)==1:
        user=users[0]
        kernel.setPredicate("lastname",user[2],sessionId)
    return res
db.close()

if __name__ == '__main__':
    CORS(app)
    app.run();