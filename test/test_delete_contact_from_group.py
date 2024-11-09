
import random



def test_delete_contact_from_group(app,db,json_groups):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(group)
        app.helper_group.submit_group_creation()
    groups=db.get_group_list()
    group = random.choice(groups)
    group_id = group.id
    group_name=group.name
    if len(db.get_contacts_in_group(group)) == 0:
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        contact_id = contact.id
        app.helper_contact.open_home_page()
        app.helper_contact.add_contact_in_group(contact_id, group_id)
    old_contacts_in_group = db.get_contacts_in_group(group)
    contact=random.choice(old_contacts_in_group)
    contact_id=contact.id
    app.helper_contact.delete_contact_on_selected_group_page(contact_id, group_id,group_name)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
    result=db.get_contacts_not_in_group(group)
    print(result)

