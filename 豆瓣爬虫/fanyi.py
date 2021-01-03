import json,os,re

source_file = 'C:/mkyn/pythonProject/豆瓣爬虫/豆瓣.csv'
json_file_result = 'D:/vuepro/json.txt'
zd_key = ["id", "name", "score", "follow", "info", "picurl"]
# 判断文件是否存在，并清空文件内容
if os.path.exists(json_file_result):
    with open(json_file_result, "r+") as f:
        f.truncate()
if os.path.isfile(source_file):
    # 处理CSV文件，将文件里的内容取出来，并组装成一个列表
    with open(source_file, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in lines:
            # 去掉首行内容（标题）
            #ifalerm = re.search('房间号', i)
            #if not ifalerm:
                l = i.strip("\n").split(",")
                # 将CSV里的内容作为字典的value，zd_k列表的内容作为字典的key
                zd = dict(zip(zd_key, l))
                data_json = json.dumps(zd, ensure_ascii=False, sort_keys=False, indent=4,
                                       separators=(',', ': '))
                # 将JSON格式的数据存储到txt文件中，便于使用
                with open(json_file_result, 'a+', encoding='utf-8') as f:
                    f.write(data_json + '\n,\n')
                    f.close()

    print("写入完成。。。。。", "\n""文件路径是：%s" % (os.path.abspath(json_file_result)))
else:
    print("文件不存在。。。。")