"""README"""
'''
v1.1:1.在v1.0基础上加入输出星座的性格特征
     2.借鉴demo后精简了代码并且判断模块函数化(simplify code and to function)
'''

sdate = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]     # 星座判断列表
conts = ['摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座',
         '处女座', '天秤座', '天蝎座', '射手座', '摩羯座']
signs = ['♑', '♒', '♓', '♈', '♉', '♊', ' ♋', '♌', '♍', '♎', '♏', '♐', '♑']
character = ["务实本分", "作天作地", "安于现状", "积极乐观", "固执内向", "圆滑世故", "多愁伤感",
             "迷之自信", "精明计较", "犹豫不决", "阴暗消极", "放荡不羁", "务实本分"]

birth = input("请输入出生日期，格式为:2001-02-21或2001-2-21\n")
birth_list = birth.split('-')  # 分割年月日到列表
month = int(birth_list[1])  # 提取月份
date = int(birth_list[2])  # 提取天数
def constellation_query(month, date):
    if date < sdate[month-1]:
        print(conts[month-1])
        print(signs[month-1])
        print(character[month-1])
    else:
        print(conts[month])
        print(signs[month])
        print(character[month])
constellation_query(month, date)
