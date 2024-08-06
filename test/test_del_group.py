from model.group import Group
def test_delete_first_group(app):
    if app.helper_group.count() ==0:
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(Group(name="ggg", header="new header", footer="new footer"))
        app.helper_group.submit_group_creation()
    old_groups = app.helper_group.get_group_list()
    app.helper_group.delete_first_group()
    new_groups = app.helper_group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
