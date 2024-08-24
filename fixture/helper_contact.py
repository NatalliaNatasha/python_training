from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.contact_cache = None

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
        self.delete_contact_by_index(0)


    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def delete_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None
        #wd.find_element_by_link_text("home").click()

    def select_edit_button(self,index):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']")[index].click()

    def modify_contact_by_index(self,index):
        wd = self.app.wd
        #self.select_contact_by_index(index)
        #wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()



    def update_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.contact_cache=None

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.go_to_home_page()
    #         self.contact_cache=[]
    #         for e in wd.find_elements_by_css_selector("tr[name='entry']"):
    #             td_value=e.find_element_by_xpath('./td[3]')
    #             td = td_value.text
    #             id = e.find_element_by_name("selected[]").get_attribute("value")
    #             self.contact_cache.append(Contact(firstname=td,id=id))
    #     return list(self.contact_cache)


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache=[]
            for row in wd.find_elements_by_name("entry"):
                cells=row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname= cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                #split a string into a list(берется текст и делится)
                all_phones=cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname,lastname=lastname,id=id,home=all_phones[0],mobilephone=all_phones[1],work=all_phones[2]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
           wd = self.app.wd
           self.go_to_home_page()
           row=wd.find_elements_by_name("entry")[index]
           cell=row.find_elements_by_tag_name("td")[6]
           cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self,index):
           wd = self.app.wd
           self.open_contact_to_edit_by_index(index)
           firstname = wd.find_element_by_name("firstname").get_attribute("value")
           lastname = wd.find_element_by_name("lastname").get_attribute("value")
           id = wd.find_element_by_name("id").get_attribute("value")
           home=wd.find_element_by_name("home").get_attribute("value")
           work = wd.find_element_by_name("work").get_attribute("value")
           mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
           return Contact(firstname=firstname, lastname=lastname,id=id,home=home,mobilephone=mobilephone,work=work)


    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text=wd.find_element_by_id("content").text
        home=re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        work=re.search("W: (.*)", text).group(1)
        return Contact(home=home, mobilephone=mobilephone,
                    work=work)






















