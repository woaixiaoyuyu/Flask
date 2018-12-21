#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 蓝图名和函数名不能重复
from flask import Blueprint, render_template, redirect

blog = Blueprint('blog', __name__)


@blog.route('/blog', methods=['GET'])
def ablog():
    return redirect("https://blog.csdn.net/qq_42192672")
