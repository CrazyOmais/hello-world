'''
安装和配置教程：https://blog.csdn.net/weixin_40522162/article/details/80677552
步骤：
1、下载0.96的easygui。https://sourceforge.net/projects/easygui/files/0.96

2、解压之后又两个文件为setup.py和easygui.py两个文件。

4、在python/Lib/site-packages文件夹下面新建easygui文件夹。

3、将easygui.py文件放入到easygui文件夹里面。

4、配置环境变量。

我的电脑–属性–高级系统设置–高级–环境变量–新建一个新的系统变量

变量名为PYTHONPATH

变量值为C:\Python\Python36-32\lib\site-packages\easygui（我的变量值是这个，每个人的路径应该不一样，具体要看安装python的安装路径） 
5、打开IDLE，引入easygui。

import easygui

6、写入测试代码。

easygui.msgbox(‘Hello World’)

7、弹出消息框。成功！
--------------------- 
作者：无驰复逸 
来源：CSDN 
原文：https://blog.csdn.net/weixin_40522162/article/details/80677552 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
import easygui

easygui.msgbox('Hello world!')
