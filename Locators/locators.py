class Locators:

    # login page objects

    username_textbox_xpath = '//input[@class="form-control site-version_ru"]'
    password_textbox_name = 'password'
    login_button_link_xpath = '//button[@class="btn btn-full btn-default btn-bold"]'
    invalidUsername_message_xpath = '//div[@class="form-line auth-result"]'
    invalidPassword_message_xpath = '//div[@class="form-line auth-result"]'
    invalidUsernameAndPassword_xpath = '//div[@class="form-line auth-result"]'

    # home page objects

    welcome_xpath = '//div[@class="personal-info__greeting"]'
    click_my_orders_xpath = '//a[@href="#orders"]'
    click_my_favorite_xpath = '//a[@href="#favorites"]'
    click_personal_data_xpath = '//a[@class="js-lk-personal-tab"]'
    register_card_xpath = '//a[@class="js-register-card-show"]'
    edit_personal_data_css_selector = "#home > div:nth-child(1) > div > div.personal-info__client > a"
    contact_info_css_selector = "#personal_form > div:nth-child(6)"
    address_info_message_css_selector = "#personal_form > div:nth-child(7) > h5.uppercase"
    subscribe_message_css_selector = "#personal_form > div:nth-child(7) > h5:nth-child(4)"
    subscribe_email_message_xpath = '//label[@for="emailSubscribe"]'
    subscribe_sms_message_xpath = '//label[@for="smsSubscribe"]'
    change_password_link_text = 'ИЗМЕНИТЬ ПАРОЛЬ'
    old_password_name = 'UF_TEMP_PASS'
    new_password_name = 'NEW_PASSWORD'
    confirmation_new_password_name = 'NEW_PASSWORD_CONFIRM'
    save_changes_name = 'save'
    basket_xpath = '//span[@id="basketCounter"]'
    catalog_products_xpath = '//*[@id="header"]/div[3]/div[1]/a'
    spets_tsena_po_karte_xpath = '//*[@id="catalog-dropdown"]/nav/a[1]'
    click_add_to_basket_xpath = '//a[contains(text(),"Перейти в корзину")]'
    click_delete_xpath = '//button[@class="order-product__btn-del"]'
    click_search = '//input[@class="search-form__item ui-autocomplete-input"]'
    click_search_button = '//i[@class="icon icon-loupe"]'
    click_adress_shop = '//a[@href="/stores/" and @class="nav__item "]'
    click_promotion = '//a[@href="/actions/" and @class="nav__item "]'
    click_card_fix_price = '//a[@href="/bonus/" and @class="nav__item "]'
    click_Pickup_store = '//a[@href="/online/" and @class="nav__item active"]'
    click_good_deeds = '//a[@href="/good-deeds/" and @class="nav__item "]'
    click_work_with_us = '#header > div.header__nav > div:nth-child(1) > nav > a:nth-child(6)'
    click_work_with_us_sklad_css_selector = 'body > div.page-header.page-header--color-bg > div > div.nav-tabs__wrap > ul > li:nth-child(2) > a'
    click_work_with_us_in_office_css_selector = 'body > div.page-header.page-header--color-bg > div > div.nav-tabs__wrap > ul > li:nth-child(3) > a'
    link_vk_xpath = '//*[@id="header"]/div[2]/div/div[1]/div[3]/a[1]/i'
    link_tiktok_xpath = '//*[@id="header"]/div[2]/div/div[1]/div[3]/a[2]/i'
    link_odnoklassniki = '//*[@id="header"]/div[2]/div/div[1]/div[3]/a[3]/i'
    link_telegram_bot_xpath = '//*[@id="header"]/div[2]/div/div[1]/div[3]/a[4]/i'
    link_youtube_xpath = '//*[@id="header"]/div[2]/div/div[1]/div[3]/a[5]/i'
    email_us_link_text = 'НАПИШИТЕ НАМ'
    close_the_form_link_text = 'НАПИШИТЕ НАМ'
    exit_xpath = '//a[@href="/work/shop/form.php?logout=yes"]'
    click_android_xpath = '//a[@href="https://play.google.com/store/apps/details?id=ru.bestprice.fixprice&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1"]'
    click_Ios = '//a[@href="https://itunes.apple.com/ru/app/fix-price/id1460007771?mt=8"]'
    click_map_page_xpath = '//a[@href="/sitemap/"]'
    click_top_logo = '//div[@class="main-brands__title"]'


