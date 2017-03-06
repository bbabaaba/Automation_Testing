# coding=utf-8
import time
import unittest2
from selenium import webdriver


class price(unittest2.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(30)

    def test_price(self):
        dr = self.dr
        dr.get("https://www.amazon.cn/")
        search_input_xpath = u"//input[@id='twotabsearchtextbox']"
        search_btn_xpath = u"//div[@class='nav-search-submit nav-sprite']/input[@class='nav-input']"
        dr.find_element_by_xpath(search_input_xpath).send_keys(u"软件测试")
        time.sleep(5)
        dr.find_element_by_xpath(search_btn_xpath).click()
        time.sleep(5)
        target_book_xpath = u"//a/h2[@data-attribute='软件测试(原书第2版)']"
        current_window_handle = dr.current_window_handle
        dr.find_element_by_xpath(target_book_xpath).click()
        time.sleep(5)
        window_handles = dr.window_handles
        for window_handle in window_handles:
            if window_handle != current_window_handle:
                dr.switch_to.window(window_handle)
        add_to_xpath = u""
        dr.find_element_by_xpath(add_to_xpath).click()
        time.sleep(5)
        # assert
        confirm_text_xpath = u"//div[@id='huc-v2-order-row-confirm-text']/h1"
        self.assertIn(u"商品已加入购物车", dr.find_element_by_xpath(confirm_text_xpath).text, "fail to judge")
        price_xpath = u"//div[@id='hlb-subcart']/div/span/span[@class='a-color-price hlb-price a-inline-block a-text-bold']"
        self.assertIn(u"20.90", dr.find_element_by_xpath(price_xpath).text, "fail to judge")

    def tearDown(self):
        self.dr.quit()
