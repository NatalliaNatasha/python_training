from model.contact import Contact
def test_delete_first_contact(app):
    if app.contact_creation.count() == 0:
        app.contact_creation.create_contact(
            Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
                    companyname="super", address="country", home="hone", mobilephone="888", work="tester",
                    fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                    page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                    amonth="March"))
    app.contact_creation.delete_first_contact()






