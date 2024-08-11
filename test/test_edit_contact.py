from model.contact import Contact
from random import randrange

def test_edit_contact(app):
    app.helper_contact.go_to_home_page()
    if app.helper_contact.count() == 0:
        app.helper_contact.create_contact(
            Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
                    companyname="super", address="country", home="hone", mobilephone="888", work="tester",
                    fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                    page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                    amonth="March"))
    old_contacts = app.helper_contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="mmm")
    contact.id = old_contacts[index].id
    app.helper_contact.modify_contact_by_index(index)
    #app.helper_contact.select_edit_button()
    app.helper_contact.fill_form(contact)
    app.helper_contact.update_contact()
    new_contacts = app.helper_contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index]=contact
    assert sorted(old_contacts,key=Contact.id_or_max)==sorted(new_contacts,key=Contact.id_or_max)





