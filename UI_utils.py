from selenium.common.exceptions import *
from selenium import webdriver
import time


def open_url(self, url):
    dr = self.dr
    try:
        dr.get(url)
        dr.maximize_window()
    except:
        print "Fail to open url: %s" % url
    finally:
        time.sleep(5)


def click(self, xpath):
    dr = self.dr
    try:
        em = dr.find_element_by_xpath(xpath)
        em.click()
    except NoSuchElementException:
        print "There is no element: %s" % xpath
    except RemoteDriverServerException:
        print "Remote driver server exception."
    except:
        print "Other exception."
    else:
        print "Click element %s successfully." % xpath
    finally:
        time.sleep(5)


def find(self, xpath):
    dr = self.dr
    try:
        em = dr.find_element_by_xpath(xpath)
        return em
    except NoSuchElementException:
        print "There is no element: %s" % xpath
    except:
        print "Other exception."
    finally:
        time.sleep(5)


def finds(self, xpath):
    dr = self.dr
    try:
        ems = dr.find_elements_by_xpath(xpath)
        return ems
    except NoSuchElementException:
        print "There is no element: %s" % xpath
    except:
        print "Other exception."
    finally:
        time.sleep(5)


def inputs(self, xpath, msg):
    dr = self.dr
    try:
        dr.find_element_by_xpath(xpath).send_keys(msg)
    except:
        print "Fail to input words: %s to element: %s" % (msg, xpath)
    else:
        print "Input words '%s' successfully." % msg
    finally:
        time.sleep(5)
