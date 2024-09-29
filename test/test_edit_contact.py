from model.contact import Contact
from random import randrange
import random

def test_edit_contact(app,db,check_ui):
    app.helper_contact.go_to_home_page()
    if len(db.get_contact_list()) == 0:
        app.helper_contact.create_contact(
            Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
                    companyname="super", address="country", home="hone", mobilephone="888", work="tester",
                    fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                    page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                    amonth="March"))
    old_contacts = db.get_contact_list()
    edit_by_id = random.choice(old_contacts)
    id_random = edit_by_id.id
    contact_new = Contact(firstname="ooo")
    contact_new.id=id_random
    app.helper_contact.modify_contact_by_id(id_random)
    app.helper_contact.fill_form(contact_new)
    app.helper_contact.update_contact()
    app.helper_contact.go_to_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts = [contact_new if contact.id == id_random else contact for contact in old_contacts]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max)==sorted(app.helper_group.get_contact_list(),key=Contact.id_or_max)


# def test_edit_contact(app):
#     app.helper_contact.go_to_home_page()
#     if app.helper_contact.count() == 0:
#         app.helper_contact.create_contact(
#             Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
#                     companyname="super", address="country", home="hone", mobilephone="888", work="tester",
#                     fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
#                     page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
#                     amonth="March"))
#     old_contacts = app.helper_contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(firstname="ooo")
#     contact.id = old_contacts[index].id
#     app.helper_contact.modify_contact_by_index(index)
#     #app.helper_contact.select_edit_button()
#     app.helper_contact.fill_form(contact)
#     app.helper_contact.update_contact()
#     app.helper_contact.go_to_home_page()
#     new_contacts = app.helper_contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[index]=contact
#     assert sorted(old_contacts,key=Contact.id_or_max)==sorted(new_contacts,key=Contact.id_or_max)




