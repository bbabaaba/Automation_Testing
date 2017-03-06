# coding=utf-8
import unittest2
from UI_utils import *


class Price(unittest2.TestCase):
    def setUp(self):
        self.dr = webdriver.Safari()
        self.dr.implicitly_wait(30)

    def test_price(self):
        dr = self.dr
        # Step 1: open url "https://www.amazon.cn/" in Firefox
        url = "https://www.amazon.cn/"
        open_url(self, url)
        # Step 2: input "软件测试"
        search_input_xpath = u"//input[@id='twotabsearchtextbox']"
        inputs(self, search_input_xpath, u"软件测试")
        # Step 3: click search button
        search_btn_xpath = u"//div[@class='nav-search-submit nav-sprite']/input[@class='nav-input']"
        click(self, search_btn_xpath)
        # Step 4: click "软件测试(原书第2版)" in result page
        target_book_xpath = u"//a/h2[@data-attribute='软件测试(原书第2版)']"
        current_window_handle = dr.current_window_handle
        click(self, target_book_xpath)
        # Step 5: click add to cart button in "软件测试(原书第2版)" page
        window_handles = dr.window_handles
        for window_handle in window_handles:
            if window_handle != current_window_handle:
                dr.switch_to.window(window_handle)
        add_to_xpath = u"//input[@id='add-to-cart-button']"
        click(self, add_to_xpath)
        # Finally, check the results;
        # 1. tips "商品已加入购物车" appears
        confirm_text_xpath = u"//div[@id='huc-v2-order-row-confirm-text']/h1"
        self.assertIn(u"商品已加入购物车", dr.find_element_by_xpath(confirm_text_xpath).text, "fail to judge")
        # 2. the price of book is "20.40"
        price_xpath = u"//div[@id='hlb-subcart']/div/span/span[@class='a-color-price hlb-price a-inline-block a-text-bold']"
        self.assertIn(u"24.50", dr.find_element_by_xpath(price_xpath).text, "fail to judge")

    def tearDown(self):
        self.dr.quit()

if __name__ == "__main__":
    unittest2.main()
