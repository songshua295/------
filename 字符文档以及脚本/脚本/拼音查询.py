# encoding='utf-8'

# Written on May 3,2024
# By Songshua295
# Function:
#           一行一个字的txt，在其后面添加上读音，用来辨别那些是没有读音的，用于剔除字库。

import csv
from pypinyin import pinyin,lazy_pinyin,Style
# from pinyin import pinyin, Style,lazy_pinyin
import os


# 输入文件和输出文件路径
input_file = '字符文档以及脚本/脚本output/table.csv'
output_file = '字符文档以及脚本/脚本output/汉字拼音对照表.csv'

# 如果输出文件已存在，则删除
if os.path.exists(output_file):
    os.remove(output_file)

# 打开输入文件并逐行处理
with open(input_file, 'r', encoding='utf-8') as f_input:
    with open(output_file, 'w', newline='', encoding='utf-8') as f_output:
        csv_writer = csv.writer(f_output)

        for line in f_input:
            # 去除换行符
            line = line.strip()
            # 查询拼音
            pinyin_result = pinyin(line, style=Style.TONE2, heteronym=True)
            
            # 如果有拼音，则写入 CSV 文件
            if pinyin_result:
                csv_writer.writerow([line, pinyin_result[0][0]])
