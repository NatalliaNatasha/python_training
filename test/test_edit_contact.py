from model.contactedit import ContactEdit

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact_creation.select_edit_button(number="9")

    app.contact_creation.edit_contact_form(ContactEdit(firstname="nine",lastname="old", amonth="March"))


