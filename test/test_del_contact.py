from model.contact import Contact
from random import randrange
import random

def test_delete_some_contact(app,db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.helper_contact.create_contact(
            Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
                    companyname="super", address="country", home="hone", mobilephone="888", work="tester",
                    fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                    page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                    amonth="March"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.helper_contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:#отключаемая проверка UI, parameter --check_ui should be added in Additional arguments
        assert sorted(new_contacts, key=Contact.id_or_max)==sorted(app.helper_group.get_contact_list(),key=Contact.id_or_max)



# def test_delete_some_contact(app):
#     if app.helper_contact.count() == 0:
#         app.helper_contact.create_contact(
#             Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
#                     companyname="super", address="country", home="hone", mobilephone="888", work="tester",
#                     fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
#                     page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
#                     amonth="March"))
#     old_contacts = app.helper_contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     app.helper_contact.delete_contact_by_index(index)
#     new_contacts = app.helper_contact.get_contact_list()
#     assert len(old_contacts) - 1 == len(new_contacts)
#     old_contacts[index:index+1] = []
#     assert old_contacts == new_contacts



