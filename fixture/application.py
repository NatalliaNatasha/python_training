from selenium import webdriver
from fixture.session import SessionHelper
from fixture.helper_group import HelperGroup
from fixture.helper_contact import HelperContact
import shutil

class Application:
    print(shutil.which("geckodriver.exe"))
    def __init__(self,browser,baseUrl):
        if browser=="firefox":
            self.wd = webdriver.Firefox()
        elif browser=="chrome":
            self.wd = webdriver.Chrome()
        elif browser=="ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session=SessionHelper(self)
        self.helper_group=HelperGroup(self)
        self.helper_contact = HelperContact(self)
        self.baseUrl=baseUrl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.baseUrl)


    def destroy(self):
        self.wd.quit()

