import MySQLdb, aiml,os

def getQA_dict(id_person):

    db = MySQLdb.connect(host="ppdatabase.ccvycmsqlp8u.eu-central-1.rds.amazonaws.com",  # your host, usually localhost
                         user="mariusdonici",  # your username
                         passwd="carrymeteodorescu",  # your password
                         db="ia")  # name of the data base

    cur = db.cursor()
    cur.execute("SELECT question_text,answer_text FROM questions join Answers join persons WHERE id_question=question_id and person_id=(%s)",(id_person))
    table = cur.fetchall()
    # print table
    db.close()
    return table

def memorate_dict(person_id,QA_dict):
    db = MySQLdb.connect(host="ppdatabase.ccvycmsqlp8u.eu-central-1.rds.amazonaws.com",  # your host, usually localhost
                         user="mariusdonici",  # your username
                         passwd="carrymeteodorescu",  # your password
                         db="ia")  # name of the data base

    cur = db.cursor()
    for key,value in QA_dict:
        cur.execute("""INSERT into questions(question_text) VALUES(%s)""",(key))
    table = cur.fetchall()
    # print table
    db.close()