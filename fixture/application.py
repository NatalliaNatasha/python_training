from selenium import webdriver
from fixture.session import SessionHelper
from fixture.helper_group import HelperGroup
from fixture.helper_contact import HelperContact

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(3)
        self.session=SessionHelper(self)
        self.helper_group=HelperGroup(self)
        self.helper_contact = HelperContact(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()

