import pymysql.cursors
from model.group import Group
from model.contact import Contact

class Dbfixture:
    def __init__(self,host,name,user,password):
        self.host=host
        self.name=name
        self.user=user
        self.password=password
        self.connection=pymysql.connect(host=host,database=name, user=user, password=password, autocommit=True)#autocommit тру -кеш сбрасывается после каждого запроса

    def get_group_list(self):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select group_id,group_name,group_header,group_footer from group_list")
            for row in cursor:
                (id,name,header,footer)=row
                list.append(Group(id=str(id),name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list




    def get_contact_list(self):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select id,firstname,middlename,lastname,nickname,title,company,address,home,homepage,"
                           "mobile,work,fax,email,email2,email3,bday,byear,ayear,bmonth,aday,amonth from addressbook")
            for row in cursor:
                (id,firstname,middlename,lastname,nickname,title,company,address,home,
                 homepage,mobile,work,fax,email,email2,email3,bday,byear,ayear,bmonth,aday,amonth)=row
                list.append(Contact(id=str(id),firstname=firstname,
                                    middlename=middlename,lastname=lastname,nickname=nickname,title=title,companyname=company,
                                    address=address,home=home,page=homepage,mobilephone=mobile,work=work,fax=fax,email=email,email2=email2,
                                    email3=email3,bday=bday,byear=byear,ayear=ayear,bmonth=bmonth,aday=aday,amonth=amonth))
        finally:
            cursor.close()
        return list



    def destroy(self):
        self.connection.close()