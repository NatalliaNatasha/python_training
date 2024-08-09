from model.group import Group

def test_edit_group(app):
    app.helper_group.open_groups_page()
    old_groups = app.helper_group.get_group_list()
    group = Group(name="edit", footer="group")
    if app.helper_group.count() ==0:
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
        app.helper_group.submit_group_creation()
    app.helper_group.init_edit_first_group()
    app.helper_group.fill_group_form(group)
    app.helper_group.submit_group_edit()
    group.id=old_groups[0].id
    new_groups = app.helper_group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0]=group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
