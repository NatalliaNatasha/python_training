from model.group import Group

class HelperGroup:
    def __init__(self,app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")))>0:
            wd.find_element_by_link_text("groups").click()


    def init_group_creation(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def change_field(self, field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name",group.name)
        self.change_field("group_header",group.header)
        self.change_field("group_footer", group.footer)


    def submit_group_creation(self):
       wd = self.app.wd
       wd.find_element_by_name("submit").click()
       self.open_groups_page()
       self.group_cache=None


    def submit_group_edit(self):
       wd = self.app.wd
       wd.find_element_by_name("update").click()
       self.open_groups_page()
       self.group_cache = None


    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def delete_group_by_index(self,index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None

    def delete_group_by_id(self,id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None

    def select_group_by_id(self,id ):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()



    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def init_edit_first_group(self):
        self.modify_group_by_index(0)


    def modify_group_by_index(self,index, group):
        wd = self.app.wd
        self.select_group_by_index(index)
        self.click_edit_group()
        # wd.find_element_by_name("group_name").click()
        # wd.find_element_by_name("group_name").clear()
        # wd.find_element_by_name("group_name").send_keys(group.name)
        # wd.find_element_by_link_text("groups").click()
        # self.select_first_group()
        # self.click_edit_group()
        self.fill_group_form(group)
        self.submit_group_edit()
        self.open_groups_page()


    def modify_group_by_id(self,id, group):
        wd = self.app.wd
        self.select_group_by_id(id)
        self.click_edit_group()
        self.fill_group_form(group)
        self.submit_group_edit()
        self.open_groups_page()



    def click_edit_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Edit group']").click()

    def fill_edited_group(self,group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)


    def modify_first_group(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        self.click_edit_group()
        self.fill_group_form(group)
        self.submit_group_edit()
        self.open_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


    group_cache=None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache=[]
            for element in wd.find_elements_by_css_selector("span.group"):
                text=element.text
                id=element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)







        














