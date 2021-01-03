import requests
import parsel
import csv #数据保存不需要安装


#1.确认数据所在地址
a=0
for page in range(0,226,25):
        url = f'https://movie.douban.com/top250?start={page}&filter='
        headers = {'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

        #2.代码请求地址数据（伪装）
        response = requests.get(url=url , headers=headers)
        #print(response.request.headers)
        html_data = response.text
        #print(html_data)

        #3.数据解析(xpath)
        #3.1转化数据类型（把html_data转化成数据对象）
        selector = parsel.Selector(html_data)
        #print(selector)

        #3.2解析数据 二次提取
        lis = selector.xpath('//ol[@class="grid_view"]/li') #提取当前所有li标签

        for li in lis:

            a=a+1
            title = li.xpath('.//div[@class="hd"]/a/span[1]/text()').get()
            score = li.xpath('.//div[@class="star"]/span[2]/text()').get()
            follow = li.xpath('.//div[@class="star"]/span[4]/text()').get()
            info = li.xpath('.//div[@class="bd"]/p[2]/span/text()').get()
            picurl = li.xpath('.//div[@class="pic"]/a/img/@src').get()
            #print(a,title,actor,score,follow,info,picurl,sep=' | ')

            #4.数据的保存
            with open('豆瓣.csv',mode='a', encoding='utf-8', newline="") as f:
               csv_write = csv.writer(f)
               csv_write.writerow([a,title,score,follow,info,picurl])

