from model.group import Group

def test_edit_group(app):
    app.helper_group.open_groups_page()
    old_groups = app.helper_group.get_group_list()
    if app.helper_group.count() ==0:
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
        app.helper_group.submit_group_creation()
    app.helper_group.init_edit_first_group()
    app.helper_group.fill_group_form(Group(name="edit", footer="group"))
    app.helper_group.submit_group_edit()
    new_groups = app.helper_group.get_group_list()
    assert len(old_groups) == len(new_groups)
