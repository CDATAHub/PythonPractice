# 导入Tkinter模块，并用别名tk引用它。
import tkinter as tk


# 定义一个函数say_hello，当按钮被点击时，这个函数会被调用。 这个函数会更新标签（label）的文本为"Hello World!"。
def say_hello():
    label.config(text="Hello World!")


# 创建一个顶级窗口（root window），这是整个GUI程序的基础。
root = tk.Tk()
# 创建一个标签（Label），设置其初始文本为"Click the button to say hello!"，并将其添加到根窗口中。
label = tk.Label(root, text="Click the button to say hello!")
label.pack()
# pack()方法用于将控件放置在父容器中，并自动调整它们的大小和位置。
# 创建一个按钮（Button），设置其文本为"SAY Hello"，并将其命令属性设置为say_hello函数。这意味着当用户点击此按钮时，say_hello函数将被调用。
button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack()
# 最后，进入主循环。在此过程中，程序会持续监听用户的操作，如点击按钮等，并作出相应的响应。
root.mainloop()
