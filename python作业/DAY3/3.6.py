import datetime
y=int(input('请输入是哪一年：'))
m=int(input('请输入月份'))
d=int(input('请输入是哪一天'))
targetDay=datetime.date(y,m,d)
dayCount=targetDay-datetime.date(targetDay.year-1,12,31)
print('%s是%s年的第%s天。'%(targetDay,y,dayCount.days))