from model.contact import Contact

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact_creation.go_to_home_page()
    app.contact_creation.select_edit_button(number="9")
    app.contact_creation.edit_contact_form(Contact(firstname="new1", middlename="new1", lastname="new1", nickname="new1", title="new1",
                            companyname="new1", address="new1", home="new1", mobilephone="0001", work="new1",
                            fax="new1", email="new1", email2="new1", email3="new1",
                            page="new1", byear="2001", ayear="2001", bday="9", bmonth="June", aday="9",
                            amonth="June"))


