from model.contact import Contact

def test_edit_contact(app):
    app.contact_creation.go_to_home_page()
    app.contact_creation.select_edit_button()
    app.contact_creation.fill_form(Contact(lastname="rrrr"))
    app.contact_creation.update_contact()



