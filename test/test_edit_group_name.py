from model.group_edit import Groupedit

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group_creation.open_groups_page()
    app.group_creation.init_edit_first_group()
    app.group_creation.fill_edited_group(Groupedit(name="Edited again"))
    app.session.logout()