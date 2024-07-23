from model.group import Group

def test_edit_group(app):
    app.group_creation.open_groups_page()
    app.group_creation.init_edit_first_group()
    app.group_creation.fill_group_form(Group(name="edit", footer="group"))
    app.group_creation.submit_group_edit()
