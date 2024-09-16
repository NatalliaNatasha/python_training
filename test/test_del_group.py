import random

from model.group import Group
from random import randrange
def test_delete_some_group(app,db,check_ui):
    if len(db.get_group_list()) ==0:
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
        app.helper_group.submit_group_creation()
    old_groups = db.get_group_list()
    group=random.choice(old_groups)
    app.helper_group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:#отключаемая проверка UI, parameter --check_ui should be added in Additional arguments
        assert sorted(new_groups, key=Group.id_or_max)==sorted(app.helper_group.get_group_list(),key=Group.id_or_max)



# def test_delete_some_group(app):
#     if app.helper_group.count() ==0:
#         app.helper_group.init_group_creation()
#         app.helper_group.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
#         app.helper_group.submit_group_creation()
#     old_groups = app.helper_group.get_group_list()
#     index=randrange(len(old_groups))
#     app.helper_group.delete_group_by_index(index)
#     new_groups = app.helper_group.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[index:index+1]=[]
#     assert old_groups == new_groups
