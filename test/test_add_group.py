# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols=string.ascii_letters+string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# testdata=[
#      Group(name=name, header=header, footer=footer)
#      for name in ["", random_string("name",10)]
#      for name in ["", random_string("header",10)]
#      for name in ["", random_string("footer",10)]
#     ]

testdata=[Group(name="", header="", footer="")]+ [
     Group(name=random_string("name",10), header=random_string("header",17),
           footer=random_string("footer",12))
     for i in range(1)
    ]


#ids=[repr(x) for x in testdata]: Этот параметр используется для присвоения каждому тесту уникального идентификатора (ID),
# который будет отображаться в выводе pytest.
@pytest.mark.parametrize("group", testdata, ids=[repr(x)for x in testdata])
def test_add_group(app,group):
    for group in testdata:
        old_groups = app.helper_group.get_group_list()
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(group)
        app.helper_group.submit_group_creation()
        assert len(old_groups) + 1 == app.helper_group.count()
        new_groups = app.helper_group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

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










