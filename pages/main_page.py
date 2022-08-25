from page_objects import PageObject, PageElement


class MainPage(PageObject):

    logo = PageElement(class_name='logo-base')
    sign_btn = PageElement(class_name='sign-btn')
    user_acc_pnl = PageElement(class_name='user-account-info')
    user_acc_pnl_2 = PageElement(xpath='//*[@id="__aer_root__"]/div/div[1]/div/span/div[4]/div[2]/div[1]')
    google_sign_btn = PageElement(class_name='nus-icon.nus-google')
    my_profile = PageElement(link_text='Мой Профиль')
    hot_product = PageElement(xpath='//*[@id="6426857680"]/div/div/div/div/a')
    cart_link = PageElement(xpath='//*[@id="header"]/div/div[2]/div[1]/a')
    wish_list = PageElement(xpath='//*[@id="__aer_root__"]/div/div[1]/div/span/div[4]/div[1]/div/a')
    quit_link = PageElement(xpath='//*[@id="__aer_root__"]/div/div[1]/div/span/div[4]/div[2]/div[2]/div/div[2]/a')
    button_sign_in = PageElement(xpath='//*[@id="__aer_root__"]/div/div[6]/div/div[2]/div/div[2]/button[2]')
    global_site_link = PageElement(xpath='//*[@id="nav-global"]/div[6]/a')
    account_eng = PageElement(xpath='//*[@id="__aer_root__"]/div/div[1]/div/span/div[4]/div[2]/div[1]/a/span/span')
    region_switcher = PageElement(id_='switcher-info')
    country_list_item = PageElement(xpath='//*[@id="nav-global"]/div[5]/div/div/div[1]/div/div[1]/ul/li[224]')
    save_button_country = PageElement(class_name='ui-button.ui-button-primary.go-contiune-btn')
    address_selector = PageElement(xpath='//*[@id="nav-global"]/div[5]/div/div/div[1]/div/a[1]')
    currency_element = PageElement(xpath='//*[@id="switcher-info"]/span[3]')
    search_button = PageElement(xpath='//*[@id="__aer_root__"]/div/div[2]/div/div/div[2]/div/form/button')
    search_input = PageElement(name='SearchText')
    customer_protection_link = PageElement(xpath='//*[@id="nav-global"]/div[2]/a')
    help_header = PageElement(xpath='//*[@id="nav-global"]/div[3]/span')
    help_header_2 = PageElement(xpath='//*[@id="__aer_root__"]/div/div[1]/div/span/div[2]/div[1]/div[1]')
    support_link = PageElement(xpath='//*[@id="nav-global"]/div[3]/ul/li[1]/a')
    complaint_link = PageElement(xpath='//*[@id="__aer_root__"]/div/div[1]/div/span/div[2]/div[1]/div[2]/ul/li[2]/a')
    app_download_link = PageElement(xpath='//*[@id="nav-global"]/div[4]/a')
    vk_sign_btn = PageElement(xpath='//*[@id="nav-user-account"]/div[2]/div[2]/p[3]/a[2]')
    electronic_link = PageElement(xpath='//*[@id="1408735750"]/div/div[1]/div/div/div[1]/a[1]')
    ali_link = PageElement(xpath='//*[@id="top-lighthouse"]/div/a')










