# encoding='utf-8'

# Written on May 3,2024
# By Songshua295
# Function:
# 将html格式中table转换成csv表格

import pandas as pd

def main():
    with open("temp\字词库文档\GBK 编码表 - 在线工具.html", "r",encoding='utf-8') as f:       ###读入文件
        htmll = f.read()
    html_data = pd.read_html(htmll)          
    for i in html_data:
        table_date = pd.DataFrame(i)
        table_date.to_csv('table.csv',encoding='utf-8-sig')
        #print table_date

if __name__ == '__main__':
    main()
