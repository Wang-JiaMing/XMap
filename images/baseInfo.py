# -*- coding: utf-8 -*-
"""
    @Time 2020/10/26 20:58
    @Author wangjiaming
    @Version V0.1
    @File Test
    @Desc:
"""

from xml.etree.ElementTree import *

unique_id = 1


# 遍历所有的节点
def walkData(root_node, level, result_list, path):
    global unique_id
    xpath = path + '/' + root_node.tag
    temp_list = [unique_id, level, root_node.tag, root_node.attrib, xpath]
    if ('xCheck' in root_node.attrib) == True:
        '以表方式进行分组归类xml标签'
        loopType='loopDot' if ('xLoopDots' in root_node.attrib) and bool((root_node.attrib['xLoopDots'])) else '-'
        rlStatus = True
        for rl in result_list:
            if rl[0] == root_node.attrib['xTable']:
                rl[2].append(temp_list)
                rlStatus = False
        if rlStatus:
            result_list.append([root_node.attrib['xTable'],loopType , [temp_list]])
    elif unique_id == 1:  # 根必进
        result_list.append(['root', '-', [temp_list]])
    unique_id += 1
    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, level + 1, result_list, xpath)
    return


def getImageXmlInfo(xml):
    level = 1  # 节点的深度从1开始
    result_list = []
    # root = fromstring(xml).getroot()
    walkData(fromstring(xml), level, result_list, '')

    return result_list
