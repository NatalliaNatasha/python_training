# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
     app.login( username="admin", password="secret")
     app.create_contact(Contact( firstname="first", middlename="middle", lastname="last", nickname="user", title="new",
                            companyname="super", address="country", home="hone", mobilephone="888", work="tester",
                            fax="7744", email="ffff@ddd.com", email2="ddddd@yy.com", email3="ddddq@tft.com",
                            page="page", byear="2010", ayear="2000", bday="1", bmonth="December", aday="1",
                            amonth="March"))
