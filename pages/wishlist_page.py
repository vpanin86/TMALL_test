from page_objects import PageObject, PageElement


class WishListPage(PageObject):

    wishlist_header = PageElement(tag_name='h2')
    wishlist_item = PageElement(xpath='//*[@id="__aer_root__"]/div/div[4]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/a')
    del_btn = PageElement(xpath='//*[@id="__aer_root__"]/div/div[4]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/a[1]')
    empty_wishlist = PageElement(xpath='//*[@id="__aer_root__"]/div/div[4]/div/div[2]/div/div/div/div/div[2]/div/span')
    create_list = PageElement(xpath='//*[@id="__aer_root__"]/div/div[4]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div/span')
    input_wishlist = PageElement(xpath='//*[@id="modalInput"]')
    input_btn = PageElement(xpath='/html/body/div[4]/div/div[2]/div/div[3]/button[1]')
    edit_list = PageElement(xpath='//*[@id="__aer_root__"]/div/div[4]/div/div[2]/div/div/div/div/div[1]/div/div/button/span')
    del_list = PageElement(xpath='//*[@id="__aer_root__"]/div/div[4]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]')
    my_list = PageElement(xpath='//*[@id="__aer_root__"]/div/div[4]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div/span[1]')
    del_list_again = PageElement(xpath='/html/body/div[4]/div/div[2]/div/button[1]')
