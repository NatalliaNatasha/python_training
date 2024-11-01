from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders
from pony.orm import db_session

class ORMFixture:

    db=Database()
    class ORMGroup(db.Entity):
        _table_='group_list' #table name
        id=PrimaryKey(int,column='group_id')
        name=Optional(str,column='group_name')
        header=Optional(str,column='group_header')
        footer=Optional(str, column='group_footer')
        contacts=Set(lambda:ORMFixture.ORMContact, table="address_in_groups",column="id",reverse="groups",lazy=True)

    class ORMContact(db.Entity):
        _table_='addressbook'
        id=PrimaryKey(int,column='id')
        firstname=Optional(str,column='firstname')
        lastname=Optional(str,column='lastname')
        deprecated=Optional(datetime, column='deprecated')
        groups=Set(lambda:ORMFixture.ORMGroup, table="address_in_groups",column="group_id",reverse="contacts",lazy=True)

    def __init__(self,host,name,user,password):
        self.db.bind('mysql',host=host,database=name, user=user, password=password)#привязка к бд
        self.db.generate_mapping()#сопоставление свойств описанных классов с таблицами и  полями таблиц
        sql_debug(True)


    def convert_groups_to_model(self,groups):
        def convert(group):
            return Group(id=str(group.id),name=group.name,header=group.header,footer=group.footer)
        return list(map (convert,groups))



    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))


    def convert_contacts_to_model(self,contacts):
        def convert(contact):
            return Contact(id=str(contact.id),firstname=contact.firstname,lastname=contact.lastname  )
        return list(map (convert,contacts))

    @db_session
    def get_contacts_in_group(self,group):
        orm_group= self.select_from_fixgroup(group)
        return self.convert_contacts_to_model(orm_group.contacts)

    def select_from_fixgroup(self, group):
        return list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.select_from_fixgroup(group)
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None
                                                     and orm_group not in c.groups))

    def destroy(self):
        pass


