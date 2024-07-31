from model.contact import Contact

def test_edit_contact(app):
    app.contact_creation.go_to_home_page()
    if app.contact_creation.count() == 0:
        app.contact_creation.create_contact(
            Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
                    companyname="super", address="country", home="hone", mobilephone="888", work="tester",
                    fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                    page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                    amonth="March"))
    app.contact_creation.select_edit_button()
    app.contact_creation.fill_form(Contact(lastname="mmm"))
    app.contact_creation.update_contact()



