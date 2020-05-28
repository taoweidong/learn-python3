#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import datetime


def generate_html(bodys, startTime, stopTime):
    env = Environment(loader=FileSystemLoader('./template'))
    template = env.get_template('mytemplate01.html')
    with open("result.html", 'w+', encoding='utf-8') as outHtml:
        html_content = template.render(start_time=startTime,
                                       stop_time=stopTime,
                                       body=bodys,
                                       Title='这是一个jinjia2模板引擎的示例代码')
        outHtml.write(html_content)


if __name__ == "__main__":
    body = []
    result = {'cabID': 1, 'shijian': 2019, 'final_result': u"正常", 'info': u"无",
              'image_path': u"test.jpg"}
    result2 = {'cabID': 2, 'shijian': 2020, 'final_result': u"异常", 'info': u"无",
               'image_path': u"test.jpg"}
    body.append(result)
    body.append(result2)

    startTime = datetime.datetime.now().strftime("%Y-%m-%d")
    stopTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    generate_html(body, startTime, stopTime)
