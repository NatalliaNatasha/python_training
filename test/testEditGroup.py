from model.group import Group

def edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group_creation.open_groups_page()
    app.group_creation.init_edit_first_group()
    app.group_creation.fill_group_form(Group(name="edit", header="old", footer="group"))
    app.group_creation.submit_group_edit()
    app.session.logout()