import time
import pytesseract
from PIL import Image
from selenium import webdriver
from time import sleep

# 创建一个浏览器
browser = webdriver.Chrome()


def breakvcode():
    # 打开古诗文网
    browser.get("https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx")
    sleep(2)  # 两秒以后
    email = browser.find_element_by_id("email")  # 获取账号input
    email.send_keys("你的账号")  # 填写账号
    time.sleep(2)
    pwd = browser.find_element_by_id("pwd")  # 获取密码input
    time.sleep(2)
    pwd.send_keys("你的密码")  # 填写密码
    time.sleep(2)
    browser.save_screenshot('static/img.png')  # 截图整个浏览器
    time.sleep(1)
    vcode = browser.find_element_by_xpath("//div[@class='mainreg2']//img[@id='imgCode']")  # 获取验证码
    print("vcode", vcode)  # 打印看一下是否获取成功标签
    print("vcode.location", vcode.location)  # 打印验证码图片坐标
    print("vcode.size", vcode.size)  # 打印验证码图片尺寸
    left = vcode.location['x']  # 左上角起点x轴坐标
    top = vcode.location['y']  # 左上角起点y轴坐标
    right = vcode.location['x'] + vcode.size['width']  # 右下角终点x轴坐标
    bottom = vcode.location['y'] + vcode.size['height']  # 右下角终点y轴坐标
    img = Image.open('static/img.png')  # 打开之前截图
    img = img.crop((left, top, right, bottom))  # 按照验证码的坐标重新截取
    img.save('static/Vcode.png')  # 保存成新的图片 此时为验证码
    image = Image.open("static/Vcode.png")  # 打开验证码图片
    image = image.convert('L')  # 把图片传入'L'，转化为灰度图像
    image.save('static/VLcode.png', 'jpeg')  # 最终的图片
    text = pytesseract.image_to_string(Image.open('static/VLcode.png'))
    print("text========", text)  # 读取图片的文字
    code = browser.find_element_by_id("code")  # 获取到验证码input
    code.send_keys(text)  # 输入验证码
    denglu = browser.find_element_by_id("denglu")  # 获取登录按钮
    denglu.click()  # 点击登录
    sleep(2)


if __name__ == '__main__':
    try:
        breakvcode()
    except Exception as e:
        print("错误", e)
        breakvcode()
