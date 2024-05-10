import requests
import re
import os
import csv

# 定义要搜索的关键词，并进行URL编码
search_word = "波分"
encoded_search_word = requests.utils.quote(search_word)
pattern = r'[A-Za-z]{3,4}'  # 编码的正则：3到4个字母

# 获取某字符串的编码
def search_and_extract(encoded_search_word):
    # 构建URL
    url = f"http://xhup.club/Xhup/Search/searchCode?search_word={encoded_search_word}&searchType=1"

    # 发送GET请求
    response = requests.get(url)

    # 检查响应状态码 解析JSON响应
    if response.status_code == 200:
        data = response.json()
        # 获取list_dz字段的值
        list1 = data["list_dz"]

        # 匹配编码正则，如果有才执行
        try:
            match = re.search(pattern, list1[0][0])
            # print(f'match：{match}')
        except IndexError:
            # 处理索引超出范围的情况
            # print(f'失败：\t{encoded_search_word}\t没有匹配到编码')
            return 'Null'
        try:
            if match:
                # 根据词的字数来返回不同的编码结果
                # print(f'len(encoded_search_word):{len(encoded_search_word)}')
                if len(encoded_search_word) == 1:
                    return re.search(pattern, list1[0][0]).group()[0:4] 
                if len(encoded_search_word) == 2:  # 二字词取两字的音码
                    # print( re.search(pattern, list1[1][0]).group()[0:2])
                    # print(re.search(pattern, list1[0][0]).group()[0:2] + re.search(pattern, list1[1][0]).group()[0:2])
                    return re.search(pattern, list1[0][0]).group()[0:2] + re.search(pattern, list1[1][0]).group()[0:2]
                if len(encoded_search_word) == 3:  # 三字词取一、二字首码，第三字前两码
                    return re.search(pattern, list1[0][0]).group()[0:1] + re.search(pattern, list1[1][0]).group()[0:1] + \
                        re.search(pattern, list1[2][0]).group()[0:2]
                if len(encoded_search_word) > 3:  # 大于三字的词取一二三首码和末尾字的首码
                    return re.search(pattern, list1[0][0]).group()[0:1] + re.search(pattern, list1[1][0]).group()[0:1] + \
                        re.search(pattern, list1[2][0]).group()[0:1] + re.search(pattern, list1[-1][0]).group()[0:1]
            else:
                # print(f"失败：\t{encoded_search_word} 未找到匹配的编码！")
                return 'Null'
        except:
                return 'Null'
    else:
        # print(f"请求失败，状态码为：{response.status_code}")
        return 'Null'


# =============================Main===========================================
originTxt = '字符文档以及脚本/tmp/方案汇总.csv'
distCSV = '字符文档以及脚本/脚本output/词组-五笔库小鹤编码2.csv'
# 如果输出文件已存在，则删除
# if os.path.exists(distCSV):
#     os.remove(distCSV)
# print(len('丏'))

print("开始=====================")

with open(originTxt, 'r',encoding='utf-8') as file:
    for line in file:
        # line = line.strip()
        line = re.sub(r'[^\u4e00-\u9fa5]+', '', line)
        # print(f'line:{line},长度:{len(line)}')
        encode=search_and_extract(line)
        with open(distCSV,mode='a+',encoding='utf-8') as output_file:
            output_file.write(line + ','+encode+'\n')
            print(f'成功：\t{line}\t编码:\t{encode}\t长度:\t{len(line)}')
        output_file.close()

# 多线程

import re
import concurrent.futures

def process_line(line):
    line = re.sub(r'[^\u4e00-\u9fa5]+', '', line)
    encode = search_and_extract(line)
    return line, encode


# with open(originTxt, 'r', encoding='utf-8') as file:
#     with open(distCSV, mode='a+', encoding='utf-8') as output_file:
#         with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
#             # 提交每一行的处理任务
#             line_tasks = [executor.submit(process_line, line) for line in file]

#             # 处理每一行的结果
#             for future in concurrent.futures.as_completed(line_tasks):
#                 line, encode = future.result()
#                 output_file.write(line + ',' + encode + '\n')
#                 print(f'成功：\t{line}\t编码:\t{encode}\t长度:\t{len(line)}')

print("===============================完成=================================================")