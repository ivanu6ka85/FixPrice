# страница пользовательского профиля
from selenium.webdriver.common.by import By
from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_xpath = Locators.welcome_xpath
        self.click_my_orders_xpath = Locators.click_my_orders_xpath
        self.click_my_favorite_xpath = Locators.click_my_favorite_xpath
        self.click_personal_data_xpath = Locators.click_personal_data_xpath
        self.click_register_card_xpath = Locators.register_card_xpath
        self.edit_personal_data_css_selector = Locators.edit_personal_data_css_selector
        self.contact_info_css_selector = Locators.contact_info_css_selector
        self.address_info_message_css_selector = Locators.address_info_message_css_selector
        self.subscribe_message_css_selector = Locators.subscribe_message_css_selector
        self.subscribe_email_message_xpath = Locators.subscribe_email_message_xpath
        self.subscribe_sms_message_xpath = Locators.subscribe_sms_message_xpath
        self.change_password_link_text = Locators.change_password_link_text
        self.new_password_name = Locators.new_password_name
        self.old_password_name = Locators.old_password_name
        self.confirmation_new_password_name = Locators.confirmation_new_password_name
        self.click_save_changes_name = Locators.save_changes_name
        self.click_basket_xpath = Locators.basket_xpath
        self.catalog_products_xpath = Locators.catalog_products_xpath
        self.spets_tsena_po_karte_xpath = Locators.spets_tsena_po_karte_xpath
        self.click_add_to_basket_xpath = Locators.click_add_to_basket_xpath
        self.click_delete_xpath = Locators.click_delete_xpath
        self.click_search_xpath = Locators.click_search
        self.click_search_button_xpath = Locators.click_search_button
        self.click_adress_shop_xpath = Locators.click_adress_shop
        self.click_promotion_xpath = Locators.click_promotion
        self.click_card_fix_price_xpath = Locators.click_card_fix_price
        self.click_Pickup_store_xpath = Locators.click_Pickup_store
        self.click_good_deeds_xpath = Locators.click_good_deeds
        self.click_work_with_us_css_selector = Locators.click_work_with_us
        self.click_work_with_us_sklad_css_selector = Locators.click_work_with_us_sklad_css_selector
        self.click_work_with_us_in_office_css_selector = Locators.click_work_with_us_in_office_css_selector
        self.link_vk_xpath = Locators.link_vk_xpath
        self.link_tiktok_xpath = Locators.link_tiktok_xpath
        self.click_link_odnoklassniki_xpath = Locators.link_odnoklassniki
        self.link_telegram_bot_xpath = Locators.link_telegram_bot_xpath
        self.link_youtube_xpath = Locators.link_youtube_xpath
        self.email_us_link_text = Locators.email_us_link_text
        self.close_the_form_link_text = Locators.close_the_form_link_text
        self.exit_xpath = Locators.exit_xpath
        self.click_android_xpath = Locators.click_android_xpath
        self.click_Ios_xpath = Locators.click_Ios
        self.click_map_page_xpath = Locators.click_map_page_xpath
        self.click_top_logo_xpath = Locators.click_top_logo





    def check_welcome_message(self):
        msg = self.driver.find_element(By.XPATH, self.welcome_xpath).text
        return msg

    def click_my_orders(self):
        self.driver.find_element(By.XPATH, self.click_my_orders_xpath).click()

    def click_my_favorite(self):
        self.driver.find_element(By.XPATH, self.click_my_favorite_xpath).click()

    def click_personal_data(self):
        self.driver.find_element(By.XPATH, self.click_personal_data_xpath).click()

    def click_register_card(self):
        self.driver.find_element(By.XPATH, self.click_register_card_xpath).click()

    def click_edit_personal_data(self):
        msg_9 = self.driver.find_element(By.CSS_SELECTOR, self.edit_personal_data_css_selector).click()
        return msg_9

    def contact_info_message(self):
        msg_10 = self.driver.find_element(By.CSS_SELECTOR, self.contact_info_css_selector).text
        return msg_10

    def delivery_info_message(self):
        msg_11 = self.driver.find_element(By.CSS_SELECTOR, self.address_info_message_css_selector).text
        return msg_11

    def other_subscribe_message(self):
        msg_12 = self.driver.find_element(By.CSS_SELECTOR, self.subscribe_message_css_selector).text
        return msg_12

    def subscribe_email_message(self):
        msg_13 = self.driver.find_element(By.XPATH, self.subscribe_email_message_xpath).click()
        return msg_13

    def subscribe_sms_message(self):
        msg_14 = self.driver.find_element(By.XPATH, self.subscribe_sms_message_xpath).click()
        return msg_14

    def click_change_password(self):
        self.driver.find_element(By.LINK_TEXT, self.change_password_link_text).click()

    def old_password_value(self):
        self.driver.find_element(By.NAME, self.old_password_name).clear()
        self.driver.find_element(By.NAME, self.old_password_name)

    def new_password_value(self):
        self.driver.find_element(By.NAME, self.new_password_name).clear()
        self.driver.find_element(By.NAME, self.new_password_name)

    def confirmation_new_password_value(self):
        self.driver.find_element(By.NAME, self.confirmation_new_password_name).clear()
        self.driver.find_element(By.NAME, self.confirmation_new_password_name)

    def click_save_changes(self):
        self.driver.find_element(By.NAME, self.click_save_changes_name).click()

    def click_catalog_products(self):
        self.driver.find_element(By.XPATH, self.catalog_products_xpath).click()

    def click_spets_tsena_po_karte(self):
        self.driver.find_element(By.XPATH, self.spets_tsena_po_karte_xpath).click()

    def click_basket(self):
        self.driver.find_element(By.XPATH, self.click_basket_xpath).click()

    def click_add_to_basket(self):
        self.driver.find_element(By.XPATH, self.click_add_to_basket_xpath).click()

    def click_delete(self):
        self.driver.find_element(By.XPATH, self.click_delete_xpath).click()

    def click_search(self):
        self.driver.find_element(By.XPATH, self.click_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.click_search_xpath)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.click_search_button_xpath).click()

    def click_adress_shop(self):
        self.driver.find_element(By.XPATH, self.click_adress_shop_xpath).click()

    def click_promotion(self):
        self.driver.find_element(By.XPATH, self.click_promotion_xpath).click()

    def click_card_fix_price(self):
        self.driver.find_element(By.XPATH, self.click_card_fix_price_xpath).click()

    def click_Pickup_store(self):
        self.driver.find_element(By.XPATH, self.click_Pickup_store_xpath).click()

    def click_good_deeds(self):
        self.driver.find_element(By.XPATH, self.click_good_deeds_xpath).click()

    def click_work_with_us(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_work_with_us_css_selector).click()

    def click_work_with_us_sklad(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_work_with_us_sklad_css_selector).click()

    def click_work_with_us_in_office(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_work_with_us_in_office_css_selector).click()


    def click_link_vk(self):
        self.driver.find_element(By.XPATH, self.link_vk_xpath).click()

    def click_link_tiktok(self):
        self.driver.find_element(By.XPATH, self.link_tiktok_xpath).click()

    def click_link_odnoklassniki(self):
        self.driver.find_element(By.XPATH, self.click_link_odnoklassniki_xpath).click()

    def click_link_telegram_bot(self):
        self.driver.find_element(By.XPATH, self.link_telegram_bot_xpath).click()

    def click_link_youtube(self):
        self.driver.find_element(By.XPATH, self.link_youtube_xpath).click()

    def click_email_us(self):
        self.driver.find_element(By.LINK_TEXT, self.email_us_link_text).click()

    def click_close_the_form(self):
        self.driver.find_element(By.LINK_TEXT, self.close_the_form_link_text).click()

    def click_exit(self):
        self.driver.find_element(By.XPATH, self.exit_xpath).click()

    def click_android(self):
        self.driver.find_element(By.XPATH, self.click_android_xpath).click()

    def click_Ios(self):
        self.driver.find_element(By.XPATH, self.click_Ios_xpath).click()

    def click_map_page(self):
        self.driver.find_element(By.XPATH, self.click_map_page_xpath).click()

    def click_top_logo(self):
        self.driver.find_element(By.XPATH, self.click_top_logo_xpath).click()







