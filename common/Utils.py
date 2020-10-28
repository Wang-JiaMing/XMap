# -*- coding: utf-8 -*-
"""
    @Time 2020/10/26 22:44
    @Author wangjiaming
    @Version V0.1
    @File Utils
    @Desc:
"""
import common.Parameter as param


def removeNameSpaces(str):
    return str.replace("{" + param.xml_namespace + "}", '')


def resetXpath(root, str):
    return str.replace(root, "").replace("{" + param.xml_namespace + "}", '')
