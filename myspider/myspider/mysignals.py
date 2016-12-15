#-*-coding:utf-8-*-

#自定义的信号
#item成功存储到数据库就发送这个信号
item_saved = object()
#item存储到数据库失败就发送这个信号
item_saved_failed = object()

#html成功存储到数据库就发送这个信号
html_saved = object()
#html存储到数据库失败就发送这个信号
html_saved_failed = object()

timeouterror = object()

dnslookuperror = object()

exceptions = object()
