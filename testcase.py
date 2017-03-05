# coding=utf-8
from selenium import webdriver
import unittest,time

class price(unittest.TestCase):
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
        title = u"软件测试(原书第2版)"
        ems = dr.find_elements_by_xpath(u"//ul/li/div/div[3]/div[1]/a")
        count = 0
        for em in ems:
            count += 1
            if em.get_attribute(u"title") == title:
                break
        add_to_cart_xpath = u"//ul/li["+ str(count) + u"]/div/div[7]/form[1]/div/span/span/input"
        dr.find_element_by_xpath(add_to_cart_xpath).click()
        time.sleep(5)
        # switch window
        confirm_text_xpath = u"//div[@id='huc-v2-order-row-confirm-text']/h1"
        if u"商品已加入购物车" in dr.find_element_by_xpath(confirm_text_xpath).text:
            assert True
        else:
            assert False
        price_xpath = u"//div[@id='hlb-subcart']/div/span/span[@class='a-color-price hlb-price a-inline-block a-text-bold']"
        if u"20.90" in dr.find_element_by_xpath(price_xpath).text:
            assert True
        else:
            assert False

    def tearDown(self):
        self.dr.quit()
