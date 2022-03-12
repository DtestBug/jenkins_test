import requests
import re

"""
path地址需要换成你存放小说的地址
x>=是从第多少章
"""


def xx():
    path = "/Users/jg-test/Downloads/"

    file = open(f'{path}洛尘.txt', 'w')  # 新创建的txt文件的存放路径 # 也可以创建一个.doc的word文档

    L_3366_ip = "https://www.9tzw.com/0_197/"

    ZhangJie_S = re.findall(re.compile('https://www.9tzw.com/0_197/.*.html'), requests.get(L_3366_ip).text)

    x = 0
    for ZhangJie in ZhangJie_S:
        x += 1

        # 从702章开始
        if x >= 1465:

            ZhangJie_data = requests.get(ZhangJie)
            ZhangJie_data.encoding = 'GBK'

            ZhangJie_name = \
                re.findall(re.compile(r"<title>.*</title>"), ZhangJie_data.text)[0].split(r'_3366洛尘张小曼_玄幻小说_九天中文')[
                    0].split(
                    ' ')[1]

            print(ZhangJie, x, ZhangJie_name)

            file.write(ZhangJie_name + "\n")

            MP = re.findall(re.compile("&nbsp;&nbsp;&nbsp;&nbsp;.*<br />"), ZhangJie_data.text)
            G1 = '一秒记住【9天中文 <a href="http://www.9TZW.COM" target="_blank" class="linkcontent">www.9TZW.COM</a> 】，无弹窗，更新快，免费阅读！'

            G2 = '加WX公众号：无名书坊，看更多小说'

            for i in MP:
                print(i)
                XS_data = i.strip('&nbsp;&nbsp;&nbsp;&nbsp;').strip('<br />')

                if G1 in XS_data:
                    S1 = XS_data.split(G1)[1]
                    file.write(S1)
                    continue

                elif G2 in XS_data:
                    S2 = XS_data.split(G2)[0]
                    file.write(S2)
                    continue

                else:
                    # print(XS_data)
                    file.write(XS_data)
                file.write("\n")
            file.write("\n\n========================\n")
        if x == 1467:
            break
