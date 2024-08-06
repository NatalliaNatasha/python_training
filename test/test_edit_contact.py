from model.contact import Contact

def test_edit_contact(app):
    app.helper_contact.go_to_home_page()
    old_contacts = app.helper_contact.get_contact_list()
    if app.helper_contact.count() == 0:
        app.helper_contact.create_contact(
            Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
                    companyname="super", address="country", home="hone", mobilephone="888", work="tester",
                    fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                    page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                    amonth="March"))
    app.helper_contact.select_edit_button()
    app.helper_contact.fill_form(Contact(lastname="mmm"))
    app.helper_contact.update_contact()
    new_contacts = app.helper_contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)



