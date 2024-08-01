from model.group import Group

def test_edit_group(app):
    app.helper_group.open_groups_page()
    if app.helper_group.count() ==0:
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
        app.helper_group.submit_group_creation()
    app.helper_group.init_edit_first_group()
    app.helper_group.fill_group_form(Group(name="edit", footer="group"))
    app.helper_group.submit_group_edit()
