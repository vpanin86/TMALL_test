from page_objects import PageObject, PageElement


class ComplaintPage(PageObject):

    customer_header = PageElement(xpath='//*[@id="root"]/div[2]/section/span[1]')
    dispute_button = PageElement(id_='submitDispute')