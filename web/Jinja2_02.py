#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader, FileSystemLoader

if __name__ == '__main__':
    """
    使用jinja2引擎框架生成HTML页面
    """
    env = Environment(loader=FileSystemLoader('./template'))
    template = env.get_template('mytemplate.html')
    print(template.render(Title='诸葛小坏'))

    with open("Hello.html", 'w+', encoding='utf-8') as fout:
        html_content = template.render(Title=u'诸葛小坏',
                                       stop_time=u'2020-05-25')
        fout.write(html_content)
