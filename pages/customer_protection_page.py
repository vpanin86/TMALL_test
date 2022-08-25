from page_objects import PageObject, PageElement


class CustomerProtectionPage(PageObject):

    customer_header = PageElement(xpath='//*[@id="root"]/div[2]/section/span[1]')