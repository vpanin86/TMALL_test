from page_objects import PageObject, PageElement


class CustomerServicePage(PageObject):

    customer_service_header = PageElement(xpath='//*[@id="ice-container"]/div/div/div[1]/div/h2')