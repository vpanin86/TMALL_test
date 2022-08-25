from page_objects import PageObject, PageElement


class ProductPage(PageObject):

    like = PageElement(xpath='//*[@id="#content"]/div[7]/button')
    like_2 = PageElement(xpath='//*[@id="#content"]/div[7]/button')
    plus_button = PageElement(xpath='//*[@id="#content"]/div[6]/div[2]/button[2]')
    minus_button = PageElement(xpath='//*[@id="#content"]/div[6]/div[2]/button[1]')
    amount = PageElement(xpath='//*[@id="#content"]/div[6]/div[2]/span[1]/span')
    max_amount = PageElement(xpath='//*[@id="#content"]/div[6]/div[2]/span[2]/span')
    xiaomi_banner = PageElement(xpath='//*[@id="__aer_root__"]/div/div/div[7]/img')
    set_selector = PageElement(xpath='//*[@id="#content"]/div[5]/div[2]/div[2]/div')
    label_set_selector = PageElement(xpath='//*[@id="#content"]/div[5]/div[1]/span[2]')
    color_selector = PageElement(xpath='//*[@id="#content"]/div[5]/div[4]/div[3]/img')
    label_color_selector = PageElement(xpath='//*[@id="#content"]/div[5]/div[3]/span[2]')
    add_to_cart_button = PageElement(xpath='//*[@id="#content"]/div[8]/div[2]/button')
    buy_now_btn = PageElement(xpath='//*[@id="#content"]/div[8]/div[1]/button')
    wishlist_link = PageElement(xpath='//*[@id="__aer_root__"]/div/div/div[1]/div/span/div[4]/div[1]/div/a')
    item_added = PageElement(xpath='/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/span')




