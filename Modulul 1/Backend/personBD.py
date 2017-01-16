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
        users=[t for t in users if t[1].lower()==first_name.lower()]
    last_name=kernel.getPredicate("last_name",id)
    if last_name!="":
        users=[t for t in users if t[2].lower()==last_name.lower()]
    status = kernel.getPredicate("status", id)
    if status != "":
        users = [t for t in users if t[3].lower() == last_name.lower()]
    city=kernel.getPredicate("city",id)
    if city!="":
        users = [t for t in users if t[4].lower() == city.lower()]
    country=kernel.getPredicate("country",id)
    if country!="":
        users = [t for t in users if t[5].lower() == country.lower()]
    nationality = kernel.getPredicate("nationality", id)
    if nationality != "":
        users = [t for t in users if t[6].lower() == nationality.lower()]
    religion = kernel.getPredicate("religion", id)
    if religion != "":
        users = [t for t in users if t[7].lower() == religion].lower()
    age = kernel.getPredicate("age", id)
    if age != "":
        users = [t for t in users if t[8] == age]
    eyes_color = kernel.getPredicate("eyes_color", id)
    if eyes_color != "":
        users = [t for t in users if t[9].lower() == eyes_color.lower()]
    hair_color = kernel.getPredicate("hair_color", id)
    if hair_color != "":
        users = [t for t in users if t[10].lower() == hair_color.lower()]
    # print users
    return users

def updateAttributes(kernel,attr,id):
    print "Updating informations about the recognized person.."
    kernel.setPredicate("first_name",attr[1],id)
    kernel.setPredicate("last_name",attr[2],id)
    kernel.setPredicate("status",attr[3],id)
    kernel.setPredicate("city", attr[4],id)
    kernel.setPredicate("country",attr[5],id)
    kernel.setPredicate("nationality",attr[6],id)
    kernel.setPredicate("religion",attr[7],id)
    kernel.setPredicate("age",attr[8],id)
    kernel.setPredicate("eyes_color",attr[9],id)
    kernel.setPredicate("hair_color", attr[10],id)


def decideToMemorate(kernel,id):
    knownItems=[]
    for item in ["first_name","last_name","status","city","country","nationality","religion","age","eyes_color","hair_color"]:
        if kernel.getPredicate(item,id)!="":
            knownItems.append(item)
def memoratePerson(kernel,id):
    print "Memorating person..."
    person_id=None
    db = MySQLdb.connect(host="ppdatabase.ccvycmsqlp8u.eu-central-1.rds.amazonaws.com",  # your host, usually localhost
                         user="mariusdonici",  # your username
                         passwd="carrymeteodorescu",  # your password
                         db="ia")  # name of the data base

    cur = db.cursor()
    print
    cur.execute("""INSERT INTO persons(first_name,last_name,status,city,country,nationality,religion,age,eyes_color,hair_color) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (kernel.getPredicate("first_name",id),
                 kernel.getPredicate("last_name", id),
                 kernel.getPredicate("status", id),
                 kernel.getPredicate("city", id),
                 kernel.getPredicate("country", id),
                 kernel.getPredicate("nationality", id),
                 kernel.getPredicate("religion", id),
                 kernel.getPredicate("age", id),
                 kernel.getPredicate("eyes_color", id),
                 kernel.getPredicate("hair_color", id)))
    db.close()