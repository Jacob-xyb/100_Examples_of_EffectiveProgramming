sdate = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]     # 星座判断列表
conts = ['摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座',
         '处女座', '天秤座', '天蝎座', '射手座', '摩羯座']
signs = ['♑', '♒', '♓', '♈', '♉', '♊', ' ♋', '♌', '♍', '♎', '♏', '♐', '♑']

birth = input("请输入出生日期，格式为:2001-02-21或2001-2-21\n")
birth_list = birth.split('-')  # 分割年月日到列表
month = int(birth_list[1])  # 提取月份
date = int(birth_list[2])  # 提取天数
if date < sdate[month-1]:
    res_c = conts[month-1]
    res_s = signs[month-1]
else:
    res_c = conts[month]
    res_s = signs[month]

print(res_c)
print(res_s)
