from model.group import Group
from random import randrange
from model.group import Group
import random

# def test_edit_group(app):
#     app.helper_group.open_groups_page()
#     if app.helper_group.count() ==0:
#         app.helper_group.init_group_creation()
#         app.helper_group.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
#         app.helper_group.submit_group_creation()
#     old_groups = app.helper_group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="edit")
#     group.id = old_groups[index].id
#     app.helper_group.modify_group_by_index(index,group)
#     new_groups = app.helper_group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group(app,db,check_ui):
    app.helper_group.open_groups_page()
    if len(db.get_group_list()) ==0:
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
        app.helper_group.submit_group_creation()
    old_groups = db.get_group_list()
    edit_by_id = random.choice(old_groups) #выбор случайной группы для редактирования
    id_random = edit_by_id.id
    group_new = Group(name="edit")
    group_new.id=id_random
    app.helper_group.modify_group_by_id(id_random, group_new)
    # group.id = old_groups[id].id
    # app.helper_group.modify_group_by_id(id,group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups = [group_new if group.id == id_random else group for group in old_groups]#замена измененной группы в старом списке
    # с использованием спискового сокращения и тернарного оператора
    if check_ui:  # отключаемая проверка UI, parameter --check_ui should be added in Additional arguments
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.helper_group.get_group_list(), key=Group.id_or_max)
