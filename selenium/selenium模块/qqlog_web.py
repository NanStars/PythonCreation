# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from lxml import etree
from selenium import webdriver
from time import sleep

# 模拟登录qq空间
# 加载谷歌驱动程序
bro = webdriver.Chrome('./chromedriver.exe')
# 访问qq空间
bro.get('https://i.qq.com/')

# 切换作用域
bro.switch_to.frame('login_frame')

# 标签定位 账号密码登录
a_tag = bro.find_element_by_id('switcher_plogin')
# 点击
a_tag.click()
# 标签定位
username_tag = bro.find_element_by_id('u')  # javascript:; javascript:;
password_tag = bro.find_element_by_id('p')
# 标签交互：
str1 = '2786683771'
username_tag.send_keys(str1)
str2 = '.@200329MLz!'
password_tag.send_keys(str2)

# 登录按钮
btn = bro.find_element_by_id('login_button')  # //*[@id="menuContainer"]/div/ul/li[3]/a  <a href="javascript:;" title="相册" tabindex="1" accesskey="4">相册</a>
btn.click()
time.sleep(1)
bro.find_element_by_link_text('相册').click()
time.sleep(1)
elements = bro.find_elements_by_class_name('gb-btn j-uploadentry-photo')
elements.click
'''
js = bro.getElementsByClassName("gb-btn j-uploadentry-photo")[0].click();
bro.execute_script(js)
'''

sleep(10)
bro.quit()
