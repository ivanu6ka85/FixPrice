# для фикстур
# python -m pytest -v --html=.\Reports\report.html --driver Chrome --driver-path D:/SkillFactory/FixPrise_Final/chromedriver.exe Tests/login.py

from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service
        cls.driver = webdriver.Chrome(
            executable_path='D:/SkillFactory/FixPrise_Final/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_invalid_username_message(self):
        """Ввод неверного логина"""
        driver = self.driver
        # driver.get('chrome://settings/')
        # driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.6);')
        # time.sleep(1)
        driver.get('https://fix-price.ru/personal/')
        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()

        login = LoginPage(driver)
        login.enter_username('6arikov80mail.ru')
        login.enter_password('Kruglik0v85')
        login.click_login()
        login.check_invalid_username_message()
        message = driver.find_element(By.XPATH, '//div[@class="form-line auth-result"]').text
        self.assertEqual(message, 'Email введен некорректно')


    def test_02_invalid_password_message(self):
        """Ввод неверного пароля"""
        driver = self.driver

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov85@mail.ru')
        login.enter_password('1234567')
        login.click_login()
        login.check_invalid_password_message()
        time.sleep(3)
        message_2 = driver.find_element(By.XPATH, '//div[@class="form-line auth-result"]').text
        self.assertEqual(message_2, 'Пользователь с таким логином и паролем не найден.')


    def test_03_invalid_username_and_password_message(self):
        """Ввод неверных логина и пароля"""
        driver = self.driver

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov80@mail.ru')
        login.enter_password('Kruqwe11rt')
        login.click_login()
        login.check_invalid_password_message()
        time.sleep(3)
        message_3 = driver.find_element(By.XPATH, '//div[@class="form-line auth-result"]').text
        self.assertEqual(message_3, 'Пользователь с таким логином и паролем не найден.')


    def test_04_login_valid(self):
        """Ввод верных логина и пароля"""
        driver = self.driver

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov85@mail.ru')
        login.enter_password('Kruglik0v85')
        login.click_login()
        time.sleep(3)
        message_4 = driver.find_element(By.XPATH, '//div[@class="personal-info__greeting"]').text
        self.assertEqual(message_4, 'ЗДРАВСТВУЙТЕ,')

    def test_05_click_my_orders(self):
        """Проверка кликабельности кнопки 'Избранные товары'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_my_orders()

        time.sleep(3)
        message_6 = driver.find_element(By.XPATH, '//a[@href="#orders"]').text
        self.assertEqual(message_6, 'МОИ ЗАКАЗЫ')

    def test_06_click_my_favorite(self):
        """Проверка кликабельности кнопки 'Избранное'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_my_favorite()

        time.sleep(3)
        message_7 = driver.find_element(By.XPATH, '//a[@href="#favorites"]').text
        self.assertEqual(message_7, 'ИЗБРАННОЕ')

    def test_07_click_personal_data(self):
        """Проверка кликабельности кнопки 'Личные данные'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_personal_data()

        message_8 = driver.find_element(By.XPATH, '//a[@class="js-lk-personal-tab"]').text
        self.assertEqual(message_8, 'ЛИЧНЫЕ ДАННЫЕ')

    def test_08_click_register_card(self):
        """Проверка кликабельности кнопки 'Зарегистрировать карту FIX-PRICE'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_register_card()

        message_9 = driver.find_element(By.XPATH, '//a[@class="js-register-card-show"]').text
        self.assertEqual(message_9, 'ЗАРЕГИСТРИРОВАТЬ КАРТУ FIX PRICE')

    def test_09_click_link_vk(self):
        """Проверка корректности кнопки с ссылкой на группу в ВК"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_link_vk()

        link_from_shop_page = driver.find_element(By.XPATH, '//a[@href="https://vk.com/fix_price" and @class="social social--sm"]').get_attribute('href')

        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_10_click_link_tiktok(self):
        """Проверка корректности кнопки с ссылкой на группу в тикток"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_link_tiktok()

        link_from_shop_page = driver.find_element(By.XPATH, '//a[@href="https://www.tiktok.com/@fixprice_russia" and @class="social social--sm"]').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_11_click_link_odnoklassniki(self):
        """Проверка корректности кнопки с ссылкой на группу в Одноклассники"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_link_odnoklassniki()

        link_from_shop_page = driver.find_element(By.XPATH, '//a[@href="https://ok.ru/fixprice" and @class="social social--sm"]').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_12_click_link_telegram_bot(self):
        """Проверка корректности кнопки с ссылкой на бота в телеграм"""
        driver = self.driver
        driver.get('https://fix-price.ru/personal/')

        homepage = HomePage(driver)
        homepage.click_link_telegram_bot()

        link_from_shop_page = driver.find_element(By.XPATH, '//a[@href="https://tgclick.com/fixprice_russia" and @class="social social--sm"]').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_13_click_link_youtube(self):
        """Проверка корректности кнопки с ссылкой на группу в ютуб"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_link_youtube()

        link_from_shop_page = driver.find_element(By.XPATH, '//a[@href="https://www.youtube.com/user/fixprice36" and @class="social social--sm"]').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_14_click_edit_personal_data(self):
        """Проверка кликабельности кнопки 'Редактировать личные данные'"""
        driver = self.driver
        driver.find_element(By.XPATH, '//i[@class="icon icon-home"]').click()

        homepage = HomePage(driver)
        homepage.click_edit_personal_data()

        message_9 = driver.find_element(By.CSS_SELECTOR, "#home > div:nth-child(1) > div > div.personal-info__client > a").text
        self.assertEqual(message_9, '')

    def test_15_contact_info_message(self):
        """Наличие контактной информации в моем профиле"""
        driver = self.driver

        message_10 = driver.find_element(By.CSS_SELECTOR, "#personal_form > div:nth-child(6)").text
        self.assertEqual(message_10, 'ЛИЧНЫЕ ДАННЫЕ\nПОЛ\nЖЕНСКИЙ\nМУЖСКОЙ\nИЗМЕНИТЬ ПАРОЛЬ')

    def test_16_address_info_message(self):
        """Наличие информации об адресе в моем профиле"""
        driver = self.driver

        message_11 = driver.find_element(By.CSS_SELECTOR, "#personal_form > div:nth-child(7) > h5.uppercase").text
        self.assertEqual(message_11, 'АДРЕС')

    def test_17_subscribe_message(self):
        """Наличие графы подписка в моем профиле"""
        driver = self.driver

        message_11 = driver.find_element(By.CSS_SELECTOR, "#personal_form > div:nth-child(7) > h5:nth-child(4)").text
        self.assertEqual(message_11, 'ПОДПИСКА')

    def test_18_subscribe_email_message(self):
        """Проверка кликабельности кнопки подписки email в моем профиле"""
        driver = self.driver

        message_12 = driver.find_element(By.XPATH, '//label[@for="emailSubscribe"]').text
        self.assertEqual(message_12, '')

    def test_19_subscribe_sms_message(self):
        """Проверка кликабельности кнопки подписки sms в моем профиле"""
        driver = self.driver

        message_13 = driver.find_element(By.XPATH, '//label[@for="smsSubscribe"]').text
        self.assertEqual(message_13, '')

    def test_20_click_change_password(self):
        """Проверка кликабельности кнопки 'Изменить пароль'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_change_password()

        message_14 = driver.find_element(By.LINK_TEXT, 'ИЗМЕНИТЬ ПАРОЛЬ').text
        self.assertEqual(message_14, 'ИЗМЕНИТЬ ПАРОЛЬ')

    def test_21_old_password_value(self):
        """Наличие поля 'Старый пароль' в графе изменить пароль"""
        driver = self.driver

        message_15 = driver.find_element(By.NAME, 'UF_TEMP_PASS').text
        self.assertEqual(message_15, '')

    def test_22_new_password_value(self):
        """Наличие поля 'Новый пароль' в графе изменить пароль"""
        driver = self.driver

        message_16 = driver.find_element(By.NAME, 'NEW_PASSWORD').text
        self.assertEqual(message_16, '')

    def test_23_confirmation_new_password_value(self):
        """Наличие поля 'Подтверждение пароля' в графе изменить пароль"""
        driver = self.driver

        message_17 = driver.find_element(By.NAME, 'NEW_PASSWORD_CONFIRM').text
        self.assertEqual(message_17, '')

    def test_24_click_save_changes(self):
        """Проверка кликабельности кнопки 'Сохранить изменения' в моём профиле"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_save_changes()

        message_18 = driver.find_element(By.NAME, 'save').text
        self.assertEqual(message_18, '')


    def test_25_click_catalog_products(self):
        """Проверка выпадающего списка при нажатие на каталог товаров"""
        driver = self.driver
        self.driver.execute_script("scroll(0, 0);")
        driver.find_element(By.XPATH, '//i[@class="icon icon-home"]').click()

        homepage = HomePage(driver)
        homepage.click_catalog_products()
        time.sleep(2)

        message_20 = driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div[1]/a').text
        self.assertEqual(message_20, "КАТАЛОГ ТОВАРОВ")

    def test_26_click_spets_tsena_po_karte(self):
        """Проверка кликабельности кнопки 'Спец цена по карте' в каталоге товаров"""
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="catalog-dropdown"]/nav/a[1]').click()

        homepage = HomePage(driver)
        homepage.spets_tsena_po_karte_xpath()

        message_21 = driver.find_element(By.XPATH, '//*[@id="catalog-dropdown"]/nav/a[1]').text
        self.assertEqual(message_21, '')

    def test_27_lens_product_and_name(self):
        """Сравнения количества товаров и названия к ним (категория 'Спец цена по карте')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product-card product-card--md')
        names = driver.find_elements(By.CLASS_NAME, 'product-card__title')

        self.assertEqual(len(products), len(names))


    def test_28_lens_product_and_button_pay(self):
        """Сравнения количества товаров и кнопки 'Купить' к ним (категория 'Спец цена по карте')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product-card product-card--md')
        button_pay = driver.find_elements(By.CLASS_NAME, 'svg-cart section-btn-cart__svg')

        self.assertEqual(len(products), len(button_pay))


    def test_29_check_buys(self):
        """Добавление товара в корзину (Подсолнечное масло "Классическое", Mr.Ricco, рафинированное, 1 л ).
        Наличие кнопки 'Перейти в корзину' в ней"""

        # товар добавляется в корзину, но тест падает.
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="catalog_sect_cont"]/div[1]/div[3]/div/div[2]/span').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//a[@class="btn btn-default btn-full"]').click()

        driver.find_element(By.XPATH, '// *[ @ id = "modalProduct"] / div / div / div[1] / div / aside / div[4] / a[1]').click()

        homepage = HomePage(driver)
        homepage.click_add_to_basket()

        time.sleep(1)
        message_24 = driver.find_element(By.CSS_SELECTOR, '#modalProduct > div > div > div:nth-child(3) > div > aside > div.order-total-bottom__btns > a.btn.btn-default.btn-full').is_displayed()
        self.assertEqual(message_24, True)



    def test_30_click_basket(self):
        """Проверка кликабельности кнопки 'В корзине'"""
        driver = self.driver
        self.driver.execute_script("scroll(0, 0);")

        homepage = HomePage(driver)
        homepage.click_basket()


        message_19 = driver.find_element(By.XPATH, '//span[@id="basketCounter"]').text
        self.assertEqual(message_19, '1 товар')

    def test_31_more_buys(self):
        """Наличие кнопки '+' для увеличения количества товара в корзине"""
        driver = self.driver

        message_25 = driver.find_element(By.XPATH, '//div[@class="btn btn-counter btn-counter--up"]').is_displayed()
        self.assertEqual(message_25, True)


    def test_32_delete_buys(self):
        """Наличие кнопки '-' для уменьшения количества товара в корзине"""
        driver = self.driver

        message_27 = driver.find_element(By.XPATH, '//div[@class="btn btn-counter btn-counter--down"]').is_displayed()
        self.assertEqual(message_27, True)


    def test_33_delete(self):
        """Наличие кнопки 'Удалить' для удаления товара из корзины"""
        driver = self.driver
        self.driver.execute_script("scroll(0, 1300);")

        message_26 = driver.find_element(By.XPATH, '//button[@class="order-product__btn-del"]').is_displayed()
        self.assertEqual(message_26, True)


    def test_34_click_delete(self):
        """Проверка кликабельности кнопки 'Удалить' в корзине"""
        # товар из корзины удаляется, но тест падает.
        driver = self.driver
        self.driver.execute_script("scroll(0, 1300);")
        time.sleep(5)

        homepage = HomePage(driver)
        homepage.click_delete()


        message_29 = driver.find_element(By.XPATH, '//button[@class="order-product__btn-del"]').text
        self.assertEqual(message_29, '')


    def test_35_click_search(self):
        """Наличие поля 'Поиска' в моём профиле"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_search()

        message_30 = driver.find_element(By.XPATH, '//input[@class="search-form__item ui-autocomplete-input"]').is_displayed()
        self.assertEqual(message_30, True)

    def test_36_click_search_button(self):
        """Проверка кликабельности кнопки 'Поиска' в корзине"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_search_button()

        message_32 = driver.find_element(By.XPATH, '//i[@class="icon icon-loupe"]').text
        self.assertEqual(message_32, '')


    def test_37_click_adress_shop(self):
        """Проверка кликабельности кнопки 'адреса магазинов'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_adress_shop()

        message_33 = driver.find_element(By.XPATH, '//a[@href="/stores/" and @class="nav__item "]').text
        self.assertEqual(message_33, 'АДРЕСА МАГАЗИНОВ')


    def test_38_click_promotion(self):
        """Проверка кликабельности кнопки 'Акции'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_promotion()

        message_36 = driver.find_element(By.XPATH, '//a[@href="/actions/" and @class="nav__item "]').text
        self.assertEqual(message_36, 'АКЦИИ')


    def test_39_click_card_fix_price(self):
        """Проверка кликабельности кнопки 'карта FixPrise' """
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_card_fix_price()

        message_36 = driver.find_element(By.XPATH, '//a[@href="/bonus/" and @class="nav__item "]').text
        self.assertEqual(message_36, 'КАРТА FIX PRICE')


    def test_40_click_Pickup_store(self):
        """Проверка кликабельности кнопки 'Самовывоз из магазина' """
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_Pickup_store()

        message_36 = driver.find_element(By.XPATH, '//a[@href="/online/" and @class="nav__item active"]').text
        self.assertEqual(message_36, 'САМОВЫВОЗ ИЗ МАГАЗИНА')

    def test_41_click_good_deeds(self):
        """Проверка кликабельности кнопки 'Добрые дела в вашем городе' """
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_good_deeds()

        message_37 = driver.find_element(By.XPATH, '//a[@href="/good-deeds/" and @class="nav__item "]').text
        self.assertEqual(message_37, 'ДОБРЫЕ ДЕЛА В ВАШЕМ ГОРОДЕ')

    def test_42_click_work_with_us(self):
        """Проверка кликабельности кнопки 'Работа у нас' """
        # кликабельность кнопки работает, тест падает
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_work_with_us()

        message_38 = driver.find_element(By.CSS_SELECTOR, '#header > div.header__nav > div:nth-child(1) > nav > a:nth-child(6)').text
        self.assertEqual(message_38, 'РАБОТА У НАС')

    def test_43_click_work_with_us_sklad(self):
        """Проверка кликабельности кнопки 'Работа на складе' """

        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_work_with_us_sklad()

        message_39 = driver.find_element(By.CSS_SELECTOR, 'body > div.page-header.page-header--color-bg > div > div.nav-tabs__wrap > ul > li:nth-child(2) > a').text
        self.assertEqual(message_39, 'РАБОТА НА СКЛАДЕ')

    def test_44_click_work_with_us_in_office(self):
        """Проверка кликабельности кнопки 'Работа на складе' """

        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_work_with_us_in_office()

        message_40 = driver.find_element(By.CSS_SELECTOR, 'body > div.page-header.page-header--color-bg > div > div.nav-tabs__wrap > ul > li:nth-child(3) > a').text
        self.assertEqual(message_40, 'РАБОТА В ОФИСЕ')


    def test_45_click_email_us(self):
        """Появления формы для отправки анкеты для приёма на работу"""
        driver = self.driver

        self.driver.execute_script("scroll(0, 1500);")

        homepage = HomePage(driver)

        time.sleep(2)
        message_46 = driver.find_element(By.XPATH, '//div[@class="office-vacancy__button-text js-toggle-button-hided-content"]').is_displayed()
        self.assertEqual(message_46, True)


    def test_46_click_exit(self):
        """Проверка кликабельности кнопки 'Выйти' """
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_exit()

        message_47 = driver.find_element(By.XPATH, '//a[@href="/work/shop/form.php?logout=yes"]').text
        self.assertEqual(message_47, '')
        time.sleep(2)

    def test_47_click_android(self):
        """Проверка кликабельности кнопки скачивания мобильного приложения на Андройд """
        driver = self.driver
        self.driver.execute_script("scroll(0, 1300);")

        homepage = HomePage(driver)
        homepage.click_android()

        message_38 = driver.find_element(By.XPATH, '//a[@href="https://play.google.com/store/apps/details?id=ru.bestprice.fixprice&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1"]').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(message_38, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_48_click_Ios(self):
        """Проверка кликабельности кнопки скачивания мобильного приложения на App Store """
        driver = self.driver
        self.driver.execute_script("scroll(0, 1300);")

        homepage = HomePage(driver)
        homepage.click_Ios()

        message_39 = driver.find_element(By.XPATH, "//a[@href='https://itunes.apple.com/ru/app/fix-price/id1460007771?mt=8']").get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(message_39, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_49_presence_brands(self):
        """Проверка, что на главной странице сайта представлены бренды, с которыми работает компания"""
        driver = self.driver
        driver.get('https://fix-price.ru/work/shop/form.php')
        self.driver.execute_script("scroll(0, 2300);")

        homepage = HomePage(driver)
        homepage.click_top_logo()

        message_49 = driver.find_element(By.XPATH, '//div[@class="main-brands__title"]').is_displayed()
        self.assertEqual(message_49, True)

    def test_50_click_map_page(self):
        """Проверка кликабельности кнопки "карта сайта" в подвале страницы """
        driver = self.driver
        driver.get('https://fix-price.ru/work/shop/form.php')
        self.driver.execute_script("scroll(0, 2500);")

        homepage = HomePage(driver)
        homepage.click_map_page()

        message_47 = driver.find_element(By.XPATH, "//a[@href='https://itunes.apple.com/ru/app/fix-price/id1460007771?mt=8']").text
        self.assertEqual(message_47, '')


    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print('Test completed')

if __name__ == '__main__':
    unittest.main()