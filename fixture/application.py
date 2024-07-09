from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group_creation import CreationGroup
from fixture.contact_creation import CreationContact

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session=SessionHelper(self)
        self.group_creation=CreationGroup(self)
        self.contact_creation = CreationContact(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()

