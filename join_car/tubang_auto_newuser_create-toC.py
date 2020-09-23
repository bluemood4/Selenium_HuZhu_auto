# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#定义登录账号
user = '15808427892'
#password = user[-6:]
password = '123456'

#设置浏览器为手机样式
mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

class TubangAutoUserJoin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_tubang_auto_user_login(self):
        driver = self.driver
        # Label: Test
        driver.get("https://tb.jytat.net/passwordlogin")
        # driver.find_element_by_css_selector("input.regInp").click()
        # driver.find_element_by_css_selector("input.regInp").clear()
        driver.find_element_by_css_selector("input.regInp").send_keys(user)
        # driver.find_element_by_xpath("//input[@type='password']").click()
        # driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        driver.find_element_by_css_selector("button.regBtn").click()
        time.sleep(3)
        driver.find_element_by_css_selector("li > img").click()#点击加入互助按钮
        driver.find_element_by_class_name("addcar").click()#点击新增车辆按钮
        time.sleep(3)
        upload = driver.find_element_by_css_selector("input.van-uploader__input")#定位到上传框
        upload.send_keys("./image/Vehicle_license.png")#发送行驶证图片
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='apply']/div[2]/ul/li[4]/input").click()#点击行驶城市框
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='apply']/div[2]/div[3]/div/div[2]/div[1]/ul/li[2]").click()#选择天津
        driver.find_element_by_xpath("//*[@id='apply']/div[2]/div[3]/div/div[2]/div[2]/ul/li").click()#选择天津直辖市
        driver.find_element_by_xpath("//*[@id='apply']/div[2]/div[3]/div/div[1]/button[2]").click()#确认行驶城市
        # driver.find_element_by_css_selector("button.van-picker__confirm").click()
        driver.find_element_by_xpath("//*[@id='apply']/div[2]/button").click()#提交
        time.sleep(3)
    
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
