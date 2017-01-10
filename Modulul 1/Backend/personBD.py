from flask import Flask
from flask_cors import CORS, cross_origin
import MySQLdb, aiml,os

def getPeopleAttributes():

    db = MySQLdb.connect(host="ppdatabase.ccvycmsqlp8u.eu-central-1.rds.amazonaws.com",  # your host, usually localhost
                         user="mariusdonici",  # your username
                         passwd="carrymeteodorescu",  # your password
                         db="ia")  # name of the data base

    cur = db.cursor()
    cur.execute("SELECT * FROM persons")
    table = cur.fetchall()
    # print table
    db.close()
    return table

def verifyExistence(kernel,id,table):
    users=table
    first_name=kernel.getPredicate("first_name", id)
    if first_name!="":
        users=[t for t in users if t[1]==first_name]

    last_name=kernel.getPredicate("last_name",id)
    if last_name!="":
        users=[t for t in users if t[2]==last_name]

    city=kernel.getPredicate("city",id)
    if city!="":
        users = [t for t in users if t[4] == city]

    country=kernel.getPredicate("country",id)
    if country!="":
        users = [t for t in users if t[5] == country]

    nationality = kernel.getPredicate("nationality", id)
    if nationality != "":
        users = [t for t in users if t[6] == nationality]

    religion = kernel.getPredicate("religion", id)
    if religion != "":
        users = [t for t in users if t[7] == religion]

    age = kernel.getPredicate("age", id)
    if age != "":
        users = [t for t in users if t[8] == age]

    eyes_color = kernel.getPredicate("eyes_color", id)
    if eyes_color != "":
        users = [t for t in users if t[9] == eyes_color]

    hair_color = kernel.getPredicate("hair_color", id)
    if hair_color != "":
        users = [t for t in users if t[9] == hair_color]
    return users

def decideToMemorate(kernel,id):
    knownItems=[]
    for item in ["first_name","last_name","status","city","country","nationality","religion","age","eyes_color","hair_color"]:
        if kernel.getPredicate(item,id)!="":
            knownItems.append(item)
def memoratePerson(kernel,id):
    person_id=None
    db = MySQLdb.connect(host="ppdatabase.ccvycmsqlp8u.eu-central-1.rds.amazonaws.com",  # your host, usually localhost
                         user="mariusdonici",  # your username
                         passwd="carrymeteodorescu",  # your password
                         db="ia")  # name of the data base

    cur = db.cursor()
    cur.execute("""INSERT INTO persons(first_name) values(%s)""",(kernel.getPredicate("first_name",id)))
    db.close()