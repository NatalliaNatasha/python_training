# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups=app.helper_group.get_group_list()
    app.helper_group.init_group_creation()
    app.helper_group.fill_group_form(Group(name ="ggg", header ="new header", footer ="new footer"))
    app.helper_group.submit_group_creation()
    new_groups=app.helper_group.get_group_list()
    assert len(old_groups)+1==len(new_groups)


def test_add_empty_group(app):
     old_groups = app.helper_group.get_group_list()
     app.helper_group.init_group_creation()
     app.helper_group.fill_group_form(Group(name ="", header ="", footer =""))
     app.helper_group.submit_group_creation()
     new_groups = app.helper_group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)










