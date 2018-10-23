# coding:utf-8
import urllib
import re


def get_html(url):
    page = urllib.urlopen(url)
    html_code = page.read()
    return html_code


def get_image(html_code):
    reg = r'src="(.+?\.jpg)" width'
    reg_img = re.compile(reg)
    img_list = reg_img.findall(html_code)
    x = 0
    for img in img_list:
        urllib.urlretrieve(img, '%s.jpg' % x)
        x += 1


print u'-------网页图片抓取-------'
print u'请输入url:',
url = raw_input()
if url:
    pass
else:
    print u'---没有地址输入正在使用默认地址---'
    url = 'http://tieba.baidu.com/p/1753935195'
print u'----------正在获取网页---------'
html_code = get_html(url)

# 写入文件用于分析
pageFile = open('pageCode.txt', 'w')  # 以写的方式打开pageCode.txt
pageFile.write(html_code)  # 写入
pageFile.close()  # 开了记得关

print u'----------正在下载图片---------'
get_image(html_code)
print u'-----------下载成功-----------'
raw_input('Press Enter to exit')
