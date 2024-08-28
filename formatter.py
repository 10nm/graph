import csv 
import re
from datetime import datetime
from collections import defaultdict
from matplotlib import pyplot as plt

import japanize_matplotlib

filePath = 'datas/statuses.csv'
date_hour_count = defaultdict(int)



startDay = 13
endDay = 27

count = 0
def readCSV(filePath):
    global count 
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 3:
                ## Format : 2000-01-01 00:00:00(.000)
                datatimestr = row[3]
                ## コンマ秒の削除
                datatimestr = re.sub(r'\.\d+', '', datatimestr)

                try:
                    # for d in range(startDay, endDay+1):        
                    s = '2024-07-{d} 00:00:00'.format(d=startDay)
                    e = '2024-08-{d} 23:59:59'.format(d=endDay) 
                    start_date = datetime.strptime(str(s), '%Y-%m-%d %H:%M:%S')
                    end_date = datetime.strptime(str(e), '%Y-%m-%d %H:%M:%S')
                    date_time_obj = datetime.strptime(datatimestr, '%Y-%m-%d %H:%M:%S')
                    if start_date <= date_time_obj <= end_date:
                        date_hour = date_time_obj.strftime('%Y-%m-%d %H:00:00')
                        date_hour_count[date_hour] += 1
                        count += 1
                except ValueError:
                    print('ValueError: ', datatimestr)
                    # 日付フォーマットが異なる場合はスキップ
                    continue


readCSV(filePath)

date_hours = sorted(date_hour_count.keys())
counts = [date_hour_count[date_hour] for date_hour in date_hours]

print(date_hours)
print(counts)

#save date_hours and counts to csv
with open('output/date_hours5.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['date_hour', 'count'])
    for i in range(len(date_hours)):
        writer.writerow([date_hours[i], counts[i]])

# hours24 = [
#     '00:00:00', 
#     '01:00:00',
#     '02:00:00',
#     '03:00:00',
#     '04:00:00',
#     '05:00:00',
#     '06:00:00',
#     '07:00:00',
#     '08:00:00',
#     '09:00:00',
#     '10:00:00',
#     '11:00:00',
#     '12:00:00',
#     '13:00:00',
#     '14:00:00',
#     '15:00:00',
#     '16:00:00',
#     '17:00:00',
#     '18:00:00',
#     '19:00:00',
#     '20:00:00',
#     '21:00:00',
#     '22:00:00',
#     '23:00:00'
# ]


# def plotDay (date, count) :
#     plt.plot(date, count, marker='o')
#     print("plot!")


# import time 
# count = []
# day = 0
# plt.figure(figsize=(10, 5))
# for i, date in enumerate(date_hours):
#     count.append (date_hour_count[date])
#     # print(count, i , date)
    
#     if (i+1) % 24 == 0:
#         print("24")
#         plotDay(date, count)
#         day += 1
#         count = []
#     # print(date, date_hour_count[date])
    



# plt.figure(figsize=(10, 5))
# # plt.plot(date_hours, counts, marker='o')
# plt.xlabel('一時間ごとの日時')
# plt.ylabel('投稿数')
# plt.title('一時間ごとの投稿数')
# plt.xticks(rotation=45)
# plt.tight_layout()

# # グラフをPNGファイルとして保存
# savename = 'output/S{s}E{e}.png'.format(s=startDay, e=endDay)
# plt.savefig(savename)

# # グラフを表示
# plt.show()

# print(count)