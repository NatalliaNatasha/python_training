from model.group import Group

def test_edit_group(app):
    app.group_creation.open_groups_page()
    if app.group_creation.count() ==0:
        app.group_creation.init_group_creation()
        app.group_creation.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
        app.group_creation.submit_group_creation()
    app.group_creation.init_edit_first_group()
    app.group_creation.fill_group_form(Group(name="edit", footer="group"))
    app.group_creation.submit_group_edit()
