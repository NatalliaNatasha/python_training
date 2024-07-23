# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group_creation.init_group_creation()
    app.group_creation.fill_group_form(Group(name ="ggg", header ="new header", footer ="new footer"))
    app.group_creation.submit_group_creation()


def test_add_empty_group(app):
     app.group_creation.init_group_creation()
     app.group_creation.fill_group_form(Group(name ="", header ="", footer =""))
     app.group_creation.submit_group_creation()










