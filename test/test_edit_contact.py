from model.contact import Contact

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact_creation.go_to_home_page()
    app.contact_creation.select_edit_button(number="9")
    app.contact_creation.fill_form(Contact(firstname="why"))
    app.contact_creation.update_contact()
    app.session.logout()


