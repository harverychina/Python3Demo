# -*- coding:utf8 -*-
# @Time：2021/11/17 10:16 上午
# @Author： Huang Jeff

from tkinter import Button, mainloop

button = Button(
    text='This is a button',
    command=lambda: print('being pressed'))
button.pack()
mainloop()

"""
函数写法

from tkiner import Button, mainloop

def print_message():
    print('being pressed')

button = Button(
    text='This is a button',
    command=print_message)

button.pack()
mainloop()
"""
