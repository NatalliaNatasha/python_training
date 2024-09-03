import json

import jsonpickle

from model.group import Group
import random
import string
import os.path
import getopt
import sys


#n-кол-во генерируемых данных,f-файл,куда это помещается
try:
    opts,args=getopt.getopt(sys.argv[1:], "n:f:",["number of groups","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=3
f="data/groups.json"

for o,a in opts:
    if o =="-n":
        n=int(a)
    elif o=="-f":
        f=a




def random_string(prefix,maxlen):
    symbols=string.ascii_letters+string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata=[Group(name="", header="", footer="")]+ [
     Group(name=random_string("name",10), header=random_string("header",17),
           footer=random_string("footer",12))
     for i in range(n)
    ]

#определение пути к  файлу
file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",f)
#открытие файла для записи
with open(file,"w") as out:
#json.dumps()конвертирует в джейсон формат, lambda x:x.__dict__ берет объект х и возвращает __dict__ атрибуты
    #out.write(json.dumps(testdata, default=lambda x:x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
