import requests,datetime,os
from lxml import etree
from datetime import datetime


# 吾爱排行榜
def get_bilibili_info():

    print('获取...')
    try:


        url = "https://www.52pojie.cn/forum.php?mod=guide&view=hot"
        ua = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        path = "C:\\Users\\用户名\\Desktop\\52pojie.txt"
        res = requests.get(url, headers=ua)
        res.encoding = 'gbk'
        html = etree.HTML(res.text)
        urls = html.xpath("//*/tr/th/a/@href")
        title = html.xpath("//*/tr/th/a/text()")
        pps=""


        for _ in range(15):
            x = str(_ + 1) + "> " + title[_] + "  >>>  " + "https://www.52pojie.cn/" + urls[_] + "\n"
            print(x)

            pps=pps+x+'\n'

        return pps



            # for i in result1:
            #
            #
            #  print(result1.index(i) + 1, i)


        print('获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None






# 	sources += x
# sources += "\n"

# with open(path,"a+") as fp:
# 	fp.write(sources)




if __name__ == '__main__':

    is_tomorrow =get_bilibili_info()
    url = 'https://service-etcne5bg-1254304775.gz.apigw.tencentcs.com/release/Wecom_push'
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
    dt = datetime.now()
    time = dt.strftime('%Y-%m-%d')
    # 'application/x-www-form-urlencoded'
    # 'application/json;charset=utf-8'
    FormData={
    'sendkey': 'akb48',
    'msg_type': 'text',
    'msg': f'[吾爱热门软件{time}]'+'\n'+'\n'+is_tomorrow

}

    res = requests.post(url=url, json=FormData)
    # content = requests.post(url=url, data=FormData).text

    print(res.text)


    print(is_tomorrow)
