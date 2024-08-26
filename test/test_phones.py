# module for regular expressions
import re

def test_phones_on_home_page(app):
    contact_from_contact_page=app.helper_contact.get_contact_list()[0]
    contact_from_edit_page=app.helper_contact.get_contact_info_from_edit_page(0)
    assert contact_from_contact_page.all_phones_from_home_page==merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_contact_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert (contact_from_contact_page.id==contact_from_edit_page.id
            and contact_from_contact_page.firstname==contact_from_edit_page.firstname
            and contact_from_contact_page.lastname==contact_from_edit_page.lastname
            and contact_from_contact_page.address==contact_from_edit_page.address)





def test_phones_on_contact_view_page(app):
     contact_from_view_page = app.helper_contact.get_contact_from_view_page(0)
     contact_from_edit_page = app.helper_contact.get_contact_info_from_edit_page(0)
     assert contact_from_view_page.home == contact_from_edit_page.home
     assert contact_from_view_page.work == contact_from_edit_page.work
     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone


def clear(s):
    #to search for a pattern in a string and replace it with a specified replacement
    return re.sub("[() -]", "",s)

def merge_phones_like_on_home_page(contact):
    #объединение  элементов итерируемого объекта в одну строку с разделителем ("\n")
    return "\n".join(filter(lambda x:x!="",
                            map(lambda x: clear(x),
                                filter(lambda x:x is not None,
                                       [contact.home,contact.mobilephone,contact.work]))))

def merge_emails_like_on_home_page(contact):
    #объединение  элементов итерируемого объекта в одну строку с разделителем ("\n")
    return "\n".join(filter(lambda x:x!="",
                            map(lambda x: clear(x),
                                filter(lambda x:x is not None,
                                       [contact.email,contact.email2,contact.email3]))))






