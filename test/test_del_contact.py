from model.contact import Contact
def test_delete_first_contact(app):
    if app.helper_contact.count() == 0:
        app.helper_contact.create_contact(
            Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
                    companyname="super", address="country", home="hone", mobilephone="888", work="tester",
                    fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                    page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                    amonth="March"))
    old_contacts = app.helper_contact.get_contact_list()
    app.helper_contact.delete_first_contact()
    new_contacts = app.helper_contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts







