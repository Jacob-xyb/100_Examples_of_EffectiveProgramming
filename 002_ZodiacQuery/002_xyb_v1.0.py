tiangan = '无、甲、乙、丙、丁、戊、己、庚、辛、壬、癸'
dizhi = '无、子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥'
zodiac = '无、鼠、牛、虎、兔、龙、蛇、马、羊、猴、鸡、狗、猪'
tiangan = tiangan.split('、')  # split 分割后返回list # strip 移除指定的字符串
dizhi = dizhi.split('、')
zodiac = zodiac.split('、')

#  公元一年：辛酉年
birth = input('请输入你的出生年月日,格式为:2001-02-21\n')
# birth = "1995-08-28"
birth = birth.split('-')
iyear = int(birth[0])

# 0001年为辛酉年
tiangan_index = iyear % 10  # % 模，求余
dizhi_index = iyear % 12

# if tiangan_index-3 > 0:
#     tiangan_res = tiangan[tiangan_index-3]
# else:
#     tiangan_res = tiangan[tiangan_index-3+10]

# if dizhi_index-3 > 0:
#     dizhi_res = dizhi[dizhi_index-3]
#     zodiac_res = zodiac[dizhi_index-3]
# else:
#     dizhi_res = dizhi[dizhi_index-3+12]
#     zodiac_res = zodiac[dizhi_index-3+12]
tiangan_res = tiangan[tiangan_index-3] \
    if tiangan_index-3 > 0 else tiangan[tiangan_index-3+10]
dizhi_res = dizhi[dizhi_index-3] \
    if dizhi_index-3 > 0 else dizhi[dizhi_index-3+12]
zodiac_res = zodiac[dizhi_index-3] \
    if dizhi_index-3 > 0 else zodiac[dizhi_index-3+12]

print('要查询的属相是:' + zodiac_res +
      '\n属相对应的年份是:' + tiangan_res + dizhi_res + '年')
