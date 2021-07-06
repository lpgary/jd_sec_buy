#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter.ttk
from tkinter import *
import win32api
import win32con

# 获得屏幕分辨率X轴
x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
# 获得屏幕分辨率Y
y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
print(f'x={x}\ny={y}'.format(x, y))
# 初始化窗口实例
root = Tk()
# 窗口命名
root.title('诶？嘿嘿')
# 设置窗口初始大小
root.geometry('640x480')
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
listb = Listbox(root)  # 创建两个列表组件
combolist = tkinter.ttk.Combobox(root)
for item in li:  # 第一个小部件插入数据
    listb.insert(0, item)
combolist['value'] = ['CSS', 'jQuery', 'Bootstrap']

listb.pack()  # 将小部件放置到主窗口中
combolist.pack()
root.mainloop()
