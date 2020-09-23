# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TubangAutoNewuserAuditing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_tubang_auto_newuser_auditing(self):
        driver = self.driver
        # Label: Test
        driver.get("http://tb.jiayibao.net/login")
        # driver.find_element_by_name("username").click()
        # driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("10000")
        # driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()#登录
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[2]/ul/li[5]/div/p/span").click()#定位到车辆审核页面
        driver.find_element_by_link_text(u"互助列表").click()#点击互助列表
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div[2]/table/tbody/tr[7]/td[8]/div/span[2]").click()#点击最新一条数据的“审核”按钮
        # driver.find_element_by_css_selector("span.el-radio__label").click()

        time.sleep(10)
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
