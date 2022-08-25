from page_objects import PageObject, PageElement


class AuthPage(PageObject):

    google_auth_body = PageElement(id_='yDmH0d')
    another_acc_link = PageElement(class_name='BHzsHc')
    email = PageElement(id_='identifierId')
    id_user = PageElement(id_='recoveryIdentifierId')
    proceed_btn_login = PageElement(xpath='//*[@id="identifierNext"]/div/button')
    proceed_btn_pass = PageElement(xpath='//*[@id="passwordNext"]/div/button')
    proceed_btn_pass_2 = PageElement(xpath='//*[@id="queryPhoneNext"]/div/button')
    proceed_btn_pass_3 = PageElement(xpath='//*[@id="collectNameNext"]/div/button')
    send_btn = PageElement(xpath='//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div/div/div/button')
    password = PageElement(class_name='whsOnd.zHQkBf')
    show_pass = PageElement(id_='selectionc0')
    invalid_pass = PageElement(class_name='EjBTad')
    invalid_login = PageElement(class_name='o6cuMc')
    sign_in = PageElement(xpath='//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[3]/div/form/button')
    checkbox = PageElement(xpath='//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/input')
    help_center_link = PageElement(xpath='//*[@id="view_container"]/div/div/div[2]/div/div[1]/span/div/div/a[1]')
    forgot_email_link = PageElement(xpath='//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/button')
    user_firstname = PageElement(id_='firstName')
    user_lastname = PageElement(id_='lastName')
    show_code_header = PageElement(xpath='//*[@id="headingText"]/span')
    list_box = PageElement(id_='lang-chooser')
    english = PageElement(xpath='//*[@id="lang-chooser"]/div[2]/div[15]/span')
    sign_in_header_eng = PageElement(xpath='//*[@id="headingText"]/span')
    vk_logo = PageElement(xpath='//*[@id="oauth_wrap_content"]/div[1]/a')








