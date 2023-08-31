import os
import re
import tkinter as tk
def search():
    # 获取用户输入的搜索内容
    input_text = input_box.get("1.0", "end-1c")  # 获取多行文本框中的所有文本
    # 将单个或多个空格和回车替换为一个加号
    output_text = re.sub(r'\s+', '+', input_text)
    # 打开浏览器搜索结果
    os.startfile(f'https://www.baidu.com/s?wd={output_text}')
    os.startfile(f'https://www.google.com/search?q={output_text}')
    os.startfile(f'https://www.bing.com/search?q={output_text}')
    os.startfile(f'https://www.zhihu.com/search?type=content&q={output_text}')
    os.startfile(f'https://search.bilibili.com/all?keyword={output_text}')
    window.quit()
 # 创建Tkinter窗口
window = tk.Tk()
window.geometry('1000x500')
window.title('搜索')
 # 添加输入框，并绑定Enter键的按下事件
input_box = tk.Text(font=("YaHei", 24))
input_box.place(relx=0.5, rely=0.4, width=600, height=300, anchor='center')
input_box.bind("<Return>", lambda event: search())  # Enter键不换行，而是执行搜索
input_box.focus_set()
 # 添加搜索按钮
search_button = tk.Button(window, text='搜索', command=search)
search_button.place(relx=0.5, rely=0.8, width=100, height=70, anchor='center')
 # 显示窗口
window.mainloop()