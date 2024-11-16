from model.contact import Contact
import random



def test_add_contact_in_group(app,db,json_groups):
    if len(db.get_group_list()) == 0:
        app.helper_group.init_group_creation()
        app.helper_group.fill_group_form(json_groups)
        app.helper_group.submit_group_creation()
    all_groups = db.get_group_list()
    group = random.choice(all_groups)
    group_id=group.id
    if len(db.get_contact_list()) == 0:
        app.helper_contact.create_contact(
            Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
                    companyname="super", address="country", home="hone", mobilephone="888", work="tester",
                    fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                    page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                    amonth="March"))
    if app.helper_contact.contact_not_in_group() is  None:
        app.helper_contact.create_contact(
            Contact(firstname="firsta", middlename="middlea", lastname="alast", nickname="auser", title="new",
                    companyname="supera", address="country", home="hone", mobilephone="888", work="tester",
                    fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                    page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                    amonth="March"))
    contacts_before_adding=db.get_contacts_in_group(group)#получили контакты из группы до добавления
    contacts_not_in_group = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts_not_in_group)#выбрали контакт из невходящих в группу
    contact_id = contact.id
    app.helper_contact.add_contact_in_group(contact_id, group_id)#добавили контакт не входящий ранее
    contacts_after_adding = db.get_contacts_in_group(group)#получили контакты после добавления
    contacts_before_adding.append(contact)
    assert sorted(contacts_before_adding, key=Contact.id_or_max) == sorted(contacts_after_adding, key=Contact.id_or_max)




