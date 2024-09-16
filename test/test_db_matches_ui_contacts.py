from model.contact import Contact


def test_contact_list(app,db):
    ui_list=app.helper_contact.get_contact_list()
    def clean(contact):
         return Contact(id=contact.id,firstname=contact.firstname.strip())#strip для удаления лишних пробелов в имени
    db_list=map(clean,db.get_contact_list())
    assert sorted(ui_list,key=Contact.id_or_max)== sorted(db_list,key=Contact.id_or_max)
