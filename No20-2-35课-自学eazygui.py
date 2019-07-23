import easygui
import sys

easygui.msgbox('我不做人了，JOJO！', title = 'DIO', ok_button = '你在说什么啊，DIO！')

if easygui.ccbox('这就是我的逃跑路线！', title = 'DIO', choices = ('OH NOOOOOOO!','抱歉，这里已经满员了')):
    easygui.msgbox('ROAD ROLLER 哒！！！', title = 'DIO', ok_button = 'WRRRYYYYYY!')
    sys.exit(0)
else:
    easygui.msgbox('呀嘞呀嘞daze~',title = '空条承太郎')
    
