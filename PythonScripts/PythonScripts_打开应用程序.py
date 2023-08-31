import os           # 操作文件和文件夹
import webbrowser   # 控制浏览器打开指定的网页
import subprocess   # 控制打开应用程序
import time         # 设置等待时间

# 打开指定的网页
webbrowser.open("https://chat.openai.com/c/a04c6b96-6391-4012-8bcf-0f8f205819b8")
webbrowser.open("https://www.bing.com/ck/a?!&&p=dc141c70b308ca01JmltdHM9MTY4MTg2MjQwMCZpZ3VpZD0xM2JjYzRlNS0wOTQzLTYxMzEtMzRjMy1kNjBhMDg2ZDYwMWMmaW5zaWQ9NTEwMA&ptn=3&hsh=3&fclid=13bcc4e5-0943-6131-34c3-d60a086d601c&u=a1L2NoYXQ_Zm9ybT1NWTAyOTEmT0NJRD1NWTAyOTE&ntb=1")

# 打开指定的文件夹
os.startfile(r"D:\dailyexe\1百度云\百度云下载\3、Java入门到起飞（含斯坦福大学练习题+力扣算法题+大厂java面试题）\入门到起飞（上）\Java基础-资料")
os.startfile(r"D:\dailyexe\1百度云\百度云下载\3、Java入门到起飞（含斯坦福大学练习题+力扣算法题+大厂java面试题）\入门到起飞（上）\Java基础-视频")

# 打开指定的 OneNote 笔记
subprocess.Popen(['C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE', 'https://d.docs.live.net/fb377632bfc0c2fc/文档/工作_面试/'])

# 等待一定时间以确保打开的网页和文件夹都已经加载完毕
time.sleep(60) # 等待 60 秒
time.sleep(12) # 再等待 12 秒

# 退出程序
''' 
webbrowser.open: 这个方法可以用来打开指定的网页，
它会在系统默认的浏览器中打开指定链接。
使用这个方法可以方便地在程序中打开特定的网页，
比如用于获取数据或者进行交互式操作等等。 

os.startfile: 这个方法可以用来打开指定的文件夹或文件，
它会在系统默认的程序中打开特定的文件夹或文件。
使用这个方法可以方便地在程序中打开特定的文件夹或文件，
比如用于访问数据文件或者配置文件等等。 
 
subprocess.Popen: 这个方法可以用来启动特定的应用程序，
它可以在指定的路径下启动特定的应用程序。
使用这个方法可以方便地在程序中启动特定的应用程序，
比如用于打开 Office 软件、调用 Python 脚本等等。 
 
time.sleep: 这个方法可以用来使程序在执行过程中暂停一段时间，
它接受一个时间参数，单位为秒。使用这个方法可以方便地进行程序等待或者延迟操作，
比如用于等待某些操作完成或者暂停程序执行等等。 
''' 