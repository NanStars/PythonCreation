# coding:utf-8
from selenium import webdriver
import pywinauto
from pywinauto.keyboard import send_keys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep


class Demo:
    def __init__(self):
        '''
        webdriver.Chrome:谷歌浏览器
        implicitly_wait(10):隐形等待10秒
        maximize_window():放大窗口
        '''

        self.device = webdriver.Chrome()
        self.device.maximize_window()
        self.device.implicitly_wait(10)

        self.device.get('https://qzone.qq.com/')

    def _log(self):
        self.switch_to.frame('login_frame')
        # 标签定位 账号密码登录
        a_tag = self.find_element_by_id('switcher_plogin')  # //*[@id="switcher_plogin"]
        # 点击
        a_tag.click()
        # 标签定位
        username_tag = self.find_element_by_id('u')
        password_tag = self.find_element_by_id('p')
        # 标签交互：
        str1 = input('请输入账号：')
        username_tag.send_keys(str1)
        str2 = input('请输入密码：')
        password_tag.send_keys(str2)
        # 登录按钮
        btn = self.find_element_by_id('login_button')
        btn.click()
        time.sleep(10)
        self.quit()


if __name__ == '__main__':
    a = Demo()
    a.log()
