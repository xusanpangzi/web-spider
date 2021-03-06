import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(lit, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            lit.append([price, title])
    except:
        print("")


def printGoodsList(lit):
    tplt = "{:4}\t{:8}\t{:6}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in lit:
        count += 1
        print(tplt.format(count, g[0], g[1]))
    print("")


def main():
    goods = '肖秀荣'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infolist, html)
        except:
            continue
    printGoodsList(infolist)


main()

