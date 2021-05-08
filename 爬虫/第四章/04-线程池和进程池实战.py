# 1。如何提取单个页面的数据
# 2.上线程池，多个页面同时抓取
import csv
from concurrent.futures import ThreadPoolExecutor

import requests
from lxml.html import etree

f = open('data.csv', 'w', encoding='utf8')
csvwriter = csv.writer(f)


def download_one_page(url):
    # 拿到页面源代码
    resp = requests.get(url)
    # print(resp.text)
    html = etree.HTML(resp.text)
    table = html.xpath('/html/body/div[2]/div[4]/div[1]/table')[0]
    # print(table)  提取到大表格
    trs = table.xpath("./tr")[1:]
    # trs = table.xpath("./tr[position()>1]")
    # 拿到每个tr
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 对数据做简单的处理 : \\ / 去掉
        # print(txt)
        txt = (item.replace("\\", "").replace("/", "") for item in txt)
        # 把数据存放在文件中
        csvwriter.writerow(txt)
    print(url, '提取完毕')


if __name__ == '__main__':
    # for i in range(1,14870):    # 效率及其低下
    #     download_one_page(f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            # 把下周任务提交给线程池
            t.submit(download_one_page, f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')

    print('全部下载完毕!')
