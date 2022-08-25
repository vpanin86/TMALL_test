from page_objects import PageObject, PageElement


class SearchPage(PageObject):

    data_product = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div[1]/div[4]/div/div[1]')
    checkbox_free_delivery = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[1]/label/span[1]')
    free_delivery_string = PageElement(class_name='snow-price_SnowPrice__freeDelivery__bz77le')
    checkbox_four_stars = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/label/span[1]')
    stars_amount = PageElement(class_name='product-snippet_ProductSnippet__score__152uer')
    min_price_input = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[1]/div[1]/div/form/input[1]')
    max_price_input = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[1]/div[1]/div/form/input[2]')
    price_button = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[1]/div[1]/div/form/button')
    product_price = PageElement(xpath='//*[@id="#content"]/div[3]/span[1]')
    product_link = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div[1]/div[4]/div/div[1]/div/div/a/div[1]/div[1]')
    app_download_link = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div[1]/div[1]/div/div[2]/div/a/img')



