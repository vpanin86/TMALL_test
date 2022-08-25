from page_objects import PageObject, PageElement


class CartPage(PageObject):

    empty_cart = PageElement(class_name='ShoppingcartStates_CartState__defaultEmpty__1ww0f')
    item_card = PageElement(class_name='ShoppingcartItemList_ProductCard__productContainer__1nl31')
    delete_item = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div/div[3]/div/div[4]/div[1]/div/button[2]')
    confirm_del_btn = PageElement(xpath='/html/body/div[4]/div/div[2]/div[2]/button[1]')
    plus_button = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div/div[3]/div/div[4]/div[2]/div[1]/div/div/button[2]')
    minus_button = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div/div[3]/div/div[4]/div[2]/div[1]/div/div/button[1]')
    amount = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div/div[3]/div/div[4]/div[2]/div[1]/div/div/input')
    delivery_header = PageElement(xpath='//*[@id="main"]/div[1]/div/p')
