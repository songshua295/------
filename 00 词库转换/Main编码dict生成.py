import requests
import re
import os
import csv

# 定义要搜索的关键词，并进行URL编码
search_word = "波分"
encoded_search_word = requests.utils.quote(search_word)
pattern = r'[A-Za-z]{3,4}'  # 编码的正则：3到4个字母


# 将数据csv转成字典，用做查询的数据库
def read_tsv_to_dict(file_path):
    data_dict = {}
    with open(file_path, newline='', encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=',')
        for row in tsvreader:
            # 假设第一列是键，第二列是值
            key = row[0]
            value = row[1]
            data_dict[key] = value
    return data_dict

# 是否已经存在，如果存在就删除
def delete_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"文件 '{file_path}' 存在并已删除。")
    else:
        print(f"文件 '{file_path}' 不存在。")

# 读取文件行数
def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        line_count = sum(1 for line in file)
    return line_count

# 获取某字符串的编码
def search_and_extract(search_word,database):
    try:
        if len(search_word) >0:
            # 根据词的字数来返回不同的编码结果
            # print(f'len(encoded_search_word):{len(encoded_search_word)}')
            if len(search_word) == 1:
                return database[search_word] 
            if len(search_word) == 2:  # 二字词取两字的音码
                return database[search_word[0:1]][0:2]+database[search_word[1]][0:2]
            if len(search_word) == 3:  # 三字词取一、二字首码，第三字前两码
                return database[search_word[0:1]][0:1]+database[search_word[1]][0:1]+database[search_word[2]][0:2]
            else:
                return database[search_word[0:1]][0:1]+database[search_word[1]][0:1]+database[search_word[2]][0:1]+database[search_word[-1]][0:1]
                # return re.search(pattern, list1[0][0]).group()[0:1] + re.search(pattern, list1[1][0]).group()[0:1] + \
                #     re.search(pattern, list1[2][0]).group()[0:1] + re.search(pattern, list1[-1][0]).group()[0:1]
        else:
            return 'Null'
    except:
            return 'Null'


# =============================Main===========================================
# 相关数据文件
dict_table = "小鹤数据表/单字码表.csv"              #用于查询的单字数据文件
source_dict="./out/sclTotxt.txt"                    #scl转成的词库txt
dict_txt = './out/生成的小鹤词库表.txt'                   #生成小鹤音形编码的输出路径
delete_file_if_exists(dict_txt)                        #判断目标文件是否存在，如果存在就删除
# 数据表生成字典
dict_data=read_tsv_to_dict(dict_table)

# print("开始=====================")

# 源词表一行一行的读取,生成的词典一行一行的写入
with open(source_dict, 'r',encoding='utf-8') as file:
    print(len(dict_table))
    for line in file:
        line = re.sub(r'[^\u4e00-\u9fa5]+', '', line)

        # 通过字典数据,查询词的编码
        encode=search_and_extract(line,dict_data)
        with open(dict_txt,mode='a+',encoding='utf-8') as output_file:
            if(encode=='Null'):
                print(f"失败:\t{line}\t有未加数据字根表的字!!!(一般是繁体等没有加入到单字码表中,需要你自行加入。)")
                
            else:
                output_file.write(encode+ '\t'+line +'\n')
                # print(f'成功：\t{line}\t编码:\t{encode}\t长度:\t{len(line)}')
                output_file.close()

print(f"完成：\t源词典：{count_lines(source_dict)}条词\t生成词典词数：\t{count_lines(dict_txt)}\n词典输出路径：\t{os.path.abspath(dict_txt)}")

# print("===============================完成=================================================")