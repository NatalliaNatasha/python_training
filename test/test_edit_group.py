from model.group import Group
from random import randrange
def test_edit_group(app):
    app.helper_group.open_groups_page()
    if app.helper_group.count() ==0:
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
        app.helper_group.submit_group_creation()
    old_groups = app.helper_group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edit", footer="group")
    group.id = old_groups[index].id
    app.helper_group.modify_group_by_index(index,group)
    new_groups = app.helper_group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


