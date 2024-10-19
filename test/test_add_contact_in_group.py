from model.contact import Contact
import random



def test_add_contact_in_group(app,db):
    all_groups = db.get_group_list()
    group = random.choice(all_groups)
    group_id=group.id
    contacts_before_adding = db.get_contacts_in_group(group)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_id = contact.id
    app.helper_contact.add_contact_in_group(contact_id,group_id)
    contacts_after_adding = db.get_contacts_in_group(group)
    contacts_before_adding.append(contact)
    assert sorted(contacts_before_adding, key=Contact.id_or_max) == sorted(contacts_after_adding, key=Contact.id_or_max)