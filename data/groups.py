from model.group import Group
# import random
# import string
# def random_string(prefix,maxlen):
#     symbols=string.ascii_letters+string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# constant=[
#       Group(name="name3", header="header3", footer="footer3"),
#       Group(name="name2", header="header2", footer="footer2")
#      ]

# testdata=[Group(name="", header="", footer="")]+ [
#      Group(name=random_string("name",10), header=random_string("header",17),
#            footer=random_string("footer",12))
#      for i in range(1)
#     ]


testdata=[
      Group(name="name3", header="header3", footer="footer3"),
      Group(name="name2", header="header2", footer="footer2")
     ]