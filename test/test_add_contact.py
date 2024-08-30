# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix,maxlen):
    symbols=string.ascii_letters+string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])





testdata=[Contact(firstname="", middlename="", lastname="",nickname="",title="",companyname="",
                  address="",home="",mobilephone="",work="",fax="", email="", email2="", email3="",
                            page="")]+ [
     Contact(firstname=random_string("firstname",10),
             middlename=random_string("middlename",17), lastname=random_string("footer",12),
             nickname=random_string("nickname",12),title=random_string("title",5),companyname=random_string("companyname",7),
             address=random_string("address",12),home=random_string("home",4),mobilephone=random_string("mobilephone",12),
             work=random_string("work",12),fax=random_string("fax",12),
             email=random_string("email",12),email2=random_string("email2",12),email3=random_string("email3",10),page=random_string("page",9),
             byear=random_string("byear",4),ayear=random_string("ayear",4)

             )
     for i in range(1)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x)for x in testdata])
def test_add_contact(app,contact):
    for contact in testdata:
        old_contacts =app.helper_contact.get_contact_list()
    # contact=Contact(firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
    #                         companyname="super", address="country", home="hone", mobilephone="888", work="tester",
    #                         fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
    #                         page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
    #                         amonth="March")
        app.helper_contact.create_contact(contact)
        new_contacts = app.helper_contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
