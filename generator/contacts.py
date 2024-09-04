import json

from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts,args=getopt.getopt(sys.argv[1:], "n:f:",["number of contacts","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=3
f="data/contacts.json"

for o,a in opts:
    if o =="-n":
        n=int(a)
    elif o=="-f":
        f=a


def random_string(prefix,maxlen):
    symbols=string.ascii_letters+string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata=[Contact(firstname="", middlename="", lastname="",nickname="",title="",companyname="",
                  address="",home="",mobilephone="",work="",fax="", email="", email2="", email3="",
                            page="")]+ [
     Contact(firstname=random_string("firstname",10),
             middlename=random_string("middlename",17), lastname=random_string("footer",12),
             nickname=random_string("nickname",12),title=random_string("title",5),companyname=random_string("companyname",7),
             address=random_string("address",12),home=random_string("home",4),mobilephone=random_string("mobilephone",12),
             work=random_string("work",12),fax=random_string("fax",12),
             email=random_string("email",12),email2=random_string("email2",12),email3=random_string("email3",10),page=random_string("page",9),
             byear=random_string("byear",4),ayear=random_string("ayear",4)

             )
     for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


