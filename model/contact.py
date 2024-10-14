from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, companyname=None, address=None, home=None,
                 mobilephone=None, work=None, fax=None, email=None, email2=None, email3=None, page=None, bday=None, byear=None, ayear=None,  bmonth=None, aday=None, amonth=None,id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None,new_group=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.companyname=companyname
        self.address=address
        self.home=home
        self.mobilephone=mobilephone
        self.work=work
        self.fax=fax
        self.email=email
        self.email2=email2
        self.email3=email3
        self.page=page
        self.bday=bday
        self.byear=byear
        self.ayear=ayear
        self.bmonth=bmonth
        self.aday=aday
        self.amonth=amonth
        self.id=id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page
        self.new_group=new_group

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id,self.firstname,self.middlename,self.lastname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id==other.id) and  self.firstname==other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
