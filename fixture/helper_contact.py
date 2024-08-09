from selenium.webdriver.support.ui import Select
from model.contact import Contact

class HelperContact:
    def __init__(self,app):
        self.app = app


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("https://localhost/addressbook/") and len(wd.find_elements_by_name("Send e-Mail"))) > 0:
            wd.get("https://localhost/addressbook/")

    def create_contact(self, contact):
        wd = self.app.wd
        wd = self.open_contact_page()
        self.fill_form(contact)
        self.submit_add_contact()

    def submit_add_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.open_home_page()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_form(self, contact):
        wd = self.app.wd
        self.type("firstname",contact.firstname)
        self.type("middlename",contact.middlename)
        self.type("lastname",contact.lastname)
        self.type("nickname",contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("company",contact.companyname)
        self.type("address",contact.address)
        wd.find_element_by_name("home").click()
        self.type("home",contact.home)
        self.type("mobile",contact.mobilephone)
        self.type("work",contact.work)
        self.type("fax",contact.fax)
        self.type("email",contact.email)
        self.type("email2",contact.email2)
        self.type("email3",contact.email3)
        self.type("homepage",contact.page)
        self.find_specific_element("bday", contact.bday)
        self.find_specific_element("bmonth",contact.bmonth)
        self.type("byear",contact.byear)
        self.find_specific_element("aday",contact.aday)
        self.find_specific_element("amonth",contact.amonth)
        self.type("ayear",contact.ayear)

    def find_specific_element(self,name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(name).click()
            wd.find_element_by_xpath("//option[@value='%s']" % str (text)).click()


    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        return wd

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_id("header").click()
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.find_element_by_link_text("home").click()

    def select_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()


    def update_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.go_to_home_page()
        contacts=[]
        for element in wd.find_elements_by_css_selector("tr[name='entry']"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text, id=id))
        return contacts











