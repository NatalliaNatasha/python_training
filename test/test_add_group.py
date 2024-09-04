# -*- coding: utf-8 -*-
from model.group import Group
import pytest
#from data.groups import testdata
#переключение на фиксированные тестовые данные
#from data.add_group import constant as testdata



#ids=[repr(x) for x in testdata]: Этот параметр используется для присвоения каждому тесту уникального идентификатора (ID),
# который будет отображаться в выводе pytest.
#@pytest.mark.parametrize("group", testdata, ids=[repr(x)for x in testdata])
# def test_add_group(app,group):
#     for group in testdata:
#         old_groups = app.helper_group.get_group_list()
#         app.helper_group.init_group_creation()
#         app.helper_group.fill_group_form(group)
#         app.helper_group.submit_group_creation()
#         assert len(old_groups) + 1 == app.helper_group.count()
#         new_groups = app.helper_group.get_group_list()
#         old_groups.append(group)
#         assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group(app,json_groups):
    group=json_groups
    old_groups = app.helper_group.get_group_list()
    app.helper_group.init_group_creation()
    app.helper_group.fill_group_form(group)
    app.helper_group.submit_group_creation()
    assert len(old_groups) + 1 == app.helper_group.count()
    new_groups = app.helper_group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)










