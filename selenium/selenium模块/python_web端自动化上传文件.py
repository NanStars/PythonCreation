# coding:utf-8
from selenium import webdriver
import pywinauto
from pywinauto.keyboard import send_keys


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
        self.device.get('https://www.wenshushu.cn/')

    def Update(self):
        '''上传文件'''
        self.device.find_element_by_css_selector('.chooice-btn span[class="text"]').click()  # 定位上传按钮
        app = pywinauto.Desktop()  # 使用pywinauto来选择文件
        dlg = app["打开"]  # 选择文件上传的窗口
        dlg["Toolbar3"].click()  # 选择文件地址输入框
        send_keys("C:\\Users\\辰\\Desktop")  # 键盘输入上传文件的路径  "C:\Users\辰\Desktop\1.txt"
        send_keys("{VK_RETURN}")  # 键盘输入回车，打开该路径
        dlg["文件名(&N):Edit"].type_keys("1.txt")  # 选中文件名输入框，输入文件名
        dlg["打开(&O)"].click()  # 点击打开


if __name__ == '__main__':
    a = Demo()
    a.Update()
