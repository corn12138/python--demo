# python中时间的处理

import time

a = int(time.time()) # 时间戳(秒)
print(a)
totalMinutes = a // 60 #分钟
print(totalMinutes)
totalHours = totalMinutes // 60 #小时
print(totalHours)
totalDays = totalHours //24 #天
print(totalDays)
totalYears = totalDays //365 #年
print(totalYears)
