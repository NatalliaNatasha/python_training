class CreationGroup:
    def __init__(self,app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
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
       self.return_to_group_page()


    def submit_group_edit(self):
       wd = self.app.wd
       wd.find_element_by_name("update").click()
       self.return_to_group_page()


    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def init_edit_first_group(self):
        wd = self.app.wd
        self.select_first_group()
        self.click_edit_group()

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



        














