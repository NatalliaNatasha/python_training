# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups=app.helper_group.get_group_list()
    group=Group(name ="ggg", header ="new header", footer ="new footer")
    app.helper_group.init_group_creation()
    app.helper_group.fill_group_form(group)
    app.helper_group.submit_group_creation()
    assert len(old_groups)+1==app.helper_group.count()
    new_groups = app.helper_group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)



# def test_add_empty_group(app):
#      old_groups = app.helper_group.get_group_list()
#      group=Group(name="", header="", footer="")
#      app.helper_group.init_group_creation()
#      app.helper_group.fill_group_form(group)
#      app.helper_group.submit_group_creation()
#      new_groups = app.helper_group.get_group_list()
#      assert len(old_groups) + 1 == len(new_groups)
#      old_groups.append(group)
#      assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)










