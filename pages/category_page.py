from page_objects import PageObject, PageElement


class CategoryPage(PageObject):

    phone_link = PageElement(xpath='//*[@id="tab-container-id"]/div[1]/div/div/div/div/div[2]/span')
