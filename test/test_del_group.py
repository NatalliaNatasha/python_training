from model.group import Group
def test_delete_first_group(app):
    if app.group_creation.count() ==0:
        app.group_creation.init_group_creation()
        app.group_creation.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
        app.group_creation.submit_group_creation()
    app.group_creation.delete_first_group()
