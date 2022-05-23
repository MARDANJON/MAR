#判断一个年份是否闰年
year = eval(input('请输入一个四位的年份:'))
# print(type(year))
# a = year%4
# b = year%100
# c = year%400
# d = 0
if (year%4==0 and year%100!=0) or (year%400==0):

	# if b != d:
	print(str(year)+' 年是闰年')
# elif c == d:
	# print(str(year)+' 年是闰年')
else:
	print(str(year)+' 年是平年')
