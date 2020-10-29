# -*- coding: utf-8 -*-
"""
    @Time 2020/10/26 20:58
    @Author wangjiaming
    @Version V0.1
    @File Test
    @Desc:
"""

from xml.etree.ElementTree import *
import traceback
import logging

unique_id = 1


# 遍历所有的节点
def __walkData(root_node, level, result_list, path):
    global unique_id
    xpath = path + '/' + root_node.tag
    temp_list = [unique_id, level, root_node.tag, root_node.attrib, xpath,
                 '' if root_node.text == None else root_node.text]
    result_list.append(temp_list)
    unique_id += 1
    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        __walkData(child, level + 1, result_list, xpath)
    return


def getSourceXmlCfg(xml):
    level = 1  # 节点的深度从1开始
    result_list = []
    try:
        __walkData(fromstring(xml), level, result_list, '')
    except Exception:
        logging.error("该数据格式不符合xml规则")
        traceback.print_exc()
    return result_list
