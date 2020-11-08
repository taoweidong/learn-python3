# -*- coding: utf-8 -*-


import win32com.client

# 最常用的模块其实是win32com.client


if __name__ == '__main__':
    print("Hello World...............")
    word = win32com.client.Dispatch('Word.Application')
    # 或者使用下面的方法，使用启动独立的进程：
    # word = win32com.client.DispatchEx('Word.Application')
    word.Visible = 0  # 后台运行
    word.DisplayAlerts = 0  # 不显示，不警告
    # 如果不声明上述属性，运行的时候会显示的打开office软件操作文档
    # 打开一个已有的word文档
    doc = word.Documents.Open("D:\\workspace\\PycharmProjects\\learn-python3\\huawei\\test.doc")
    # new_doc = word.Documents.Add() # 创建新的word文档
    # self.xlApp.Selection.Find.ClearFormatting()
    # self.xlApp.Selection.Find.Replacement.ClearFormatting()

    word.Selection.Find.ClearFormatting()
    word.Selection.Find.Replacement.ClearFormatting()
    word.Selection.Find.Execute("习近平", False, False, False, False, False, True, 1, True, "习大大", 2)

    doc.Save()  # 保存
    doc.Close()  # 关闭 word 文档
    word.Quit()  # 关闭 office
    # print("word do success ...........")
    name = input("word do success ...........")
    # print(name)
