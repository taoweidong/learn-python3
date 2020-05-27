#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from jinja2 import Template

if __name__ == '__main__':
    template = Template("Hello  {{ name }}")
    print(template.render(name='Jony'))
