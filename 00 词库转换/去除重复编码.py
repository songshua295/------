def remove_duplicate_lines(file_path):
    # 读取文件内容并去除重复行
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = list(set(lines))

    # 写入去重后的内容到同一文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# 假设dict_txt是一个变量，存储了文件路径
dict_txt = input("请输入文件路径：")  # 请替换成你的文件路径
remove_duplicate_lines(dict_txt)