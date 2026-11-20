# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(locator, timeout=10):
    '''等到元素加载完成'''
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


driver = webdriver.Chrome()
driver.get('https://i.qq.com/')
driver.switch_to.frame('login_frame')

# 标签定位 账号密码登录
a_tag = driver.find_element_by_id('switcher_plogin')
# 点击
a_tag.click()
# 标签定位
username_tag = driver.find_element_by_id('u')#javascript:; javascript:;
password_tag = driver.find_element_by_id('p')
# 标签交互：
str1 = '1546832768'
username_tag.send_keys(str1)
str2 = '.@200329Mlz!'
password_tag.send_keys(str2)

# 登录按钮
btn = driver.find_element_by_id('login_button')#//*[@id="menuContainer"]/div/ul/li[3]/a  <a href="javascript:;" title="相册" tabindex="1" accesskey="4">相册</a>  javascript:;
btn.click()

locator = (By.CLASS_NAME, 'custom_menu_swf')  # 相当于find_elements_by_class_name     //*[@id="menuContainer"]/div/div/ul/li[3]/a
wait(locator)
elements = driver.find_elements_by_class_name('custom_menu_swf')
link = []
linkNum = len(elements)
for i in range(linkNum):
    wait(locator)
    elements = driver.find_elements_by_class_name('custom_menu_swf')  # 再次获取元素，预防StaleElementReferenceException   #//*[@id="menuContainer"]/div/div/ul/li[3]/a
    driver.execute_script('arguments[0].click();', elements[i])  # 模拟用户点击
    time.sleep()
    print(i, driver.current_url)
    link.append(driver.current_url)
    time.sleep(0.01)  # 留时间给页面后退，网不好调大点，此处用driver.implicitly_wait()无效
    driver.back()

driver.quit()
print('共{}条链接'.format(len(link)))
