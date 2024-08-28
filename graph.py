import csv
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルのパス
file_path_all = 'output/date_hours5.csv'
file_path_kyy = 'output/date_hours_kkk.csv'
file_path_hyj = 'output/date_hours1.csv'

# データを格納する辞書
data = defaultdict(list)
hourly_counts = defaultdict(list)
hourly_countskyy = defaultdict(list)
hourly_countshyj = defaultdict(list)

# CSVファイルを読み込む
with open(file_path_all, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # ヘッダーをスキップ
    for row in reader:
        date_hour = row[0]
        count = int(row[1])
        date = datetime.strptime(date_hour, '%Y-%m-%d %H:%M:%S').date()
        hour = datetime.strptime(date_hour, '%Y-%m-%d %H:%M:%S').strftime('%H:00:00')
        data[date].append((hour, count))
        hourly_counts[hour].append(count)

# # CSVファイルを読み込む
# with open(file_path_kyy, 'r') as file:
#     reader = csv.reader(file)
#     next(reader)  # ヘッダーをスキップ
#     for row in reader:
#         date_hour = row[0]
#         count = int(row[1])
#         date = datetime.strptime(date_hour, '%Y-%m-%d %H:%M:%S').date()
#         hour = datetime.strptime(date_hour, '%Y-%m-%d %H:%M:%S').strftime('%H:00:00')
#         data[date].append((hour, count))
#         hourly_countskyy[hour].append(count)

# # CSVファイルを読み込む
# with open(file_path_hyj, 'r') as file:
#     reader = csv.reader(file)
#     next(reader)  # ヘッダーをスキップ
#     for row in reader:
#         date_hour = row[0]
#         count = int(row[1])
#         date = datetime.strptime(date_hour, '%Y-%m-%d %H:%M:%S').date()
#         hour = datetime.strptime(date_hour, '%Y-%m-%d %H:%M:%S').strftime('%H:00:00')
#         data[date].append((hour, count))
#         hourly_countshyj[hour].append(count)

# グラフの設定
plt.figure(figsize=(14, 8))
hours24 = [
    '00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00',
    '06:00:00', '07:00:00', '08:00:00', '09:00:00', '10:00:00', '11:00:00',
    '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00', '17:00:00',
    '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00'
]

# 各日のデータをプロット
for date, counts in data.items():
    counts_sorted = sorted(counts, key=lambda x: x[0])
    hours = [hour for hour, count in counts_sorted]
    counts = [count for hour, count in counts_sorted]
    plt.plot(hours, counts, marker='o', label=str(date))

# 時間ごとの平均値を計算
average_counts = [sum(hourly_counts[hour]) / len(hourly_counts[hour]) for hour in hours24]

# average_countskyy = [sum(hourly_countskyy[hour]) / len(hourly_countskyy[hour]) for hour in hours24]

# average_countshyj = [sum(hourly_countshyj[hour]) / len(hourly_countshyj[hour]) for hour in hours24]

# 平均値をプロット
plt.plot(hours24, average_counts, marker='x', linestyle='--', label='全日平均')
# plt.plot(hours24, average_countskyy, marker='x', linestyle='--',  label='休日平均')
# plt.plot(hours24, average_countshyj, marker='x', linestyle='--',  label='平日平均')

# グラフのラベルとタイトル
plt.xlabel('時間')
plt.ylabel('投稿数')
plt.title('すべての投稿数の比較')
plt.xticks(hours24, rotation=45)
plt.legend(loc='center right')
plt.tight_layout()

# グラフを保存
plt.savefig('output/graph-all.png')
# グラフを表示
plt.show()