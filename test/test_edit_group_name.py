from model.group import Group

def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group_creation.modify_first_group(Group(name="again"))
    app.session.logout()

def test_modify_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group_creation.modify_first_group(Group(header="best"))
    app.session.logout()