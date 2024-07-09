# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group_creation.init_group_creation()
    app.group_creation.fill_group_form(Group(name = "ggg", header = "new header", footer = "new footer"))
    app.group_creation.submit_group_creation()
    app.session.logout()

def test_add_empty_group(app):
     app.session.login( username="admin",password= "secret")
     app.group_creation.init_group_creation()
     app.group_creation.fill_group_form(Group(name = "", header = "", footer = ""))
     app.group_creation.submit_group_creation()
     app.session.logout()









