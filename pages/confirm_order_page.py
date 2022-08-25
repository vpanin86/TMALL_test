from page_objects import PageObject, PageElement


class ConfirmOrder(PageObject):

    delivery_header = PageElement(xpath='//*[@id="main"]/div[1]/div/p')
    plus_button = PageElement(xpath='//*[@id="main"]/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[1]/span/span/span[3]/button')
    minus_button = PageElement(xpath='//*[@id="main"]/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[1]/span/span/span[1]/button')
    amount = PageElement(xpath='//*[@id="main"]/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[1]/span/span/span[2]/input')