# -*- coding: utf-8 -*-
"""
    @Time 2020/10/26 20:58
    @Author wangjiaming
    @Version V0.1
    @File Test
    @Desc:
"""

from xml.etree.ElementTree import *
import xCommon.utils as utils

unique_id = 1


# 遍历所有的节点
def __walkData(root_node, level, result_list, all_list, path):
    global unique_id
    xpath = path + '/' + root_node.tag
    temp_list = [unique_id, level, root_node.tag, root_node.attrib, xpath]
    if ('xCheck' in root_node.attrib) == True:
        '以表方式进行分组归类xml标签'
        loopType = 'loopDot' if ('xLoopDots' in root_node.attrib) and bool((root_node.attrib['xLoopDots'])) else '-'
        rlStatus = True
        for rl in result_list:
            if rl[0] == root_node.attrib['xTable']:
                rl[2].append(temp_list)
                rlStatus = False
        if rlStatus:
            result_list.append([root_node.attrib['xTable'], loopType, [temp_list]])
    elif unique_id == 1:  # 根必进
        result_list.append(['root', '-', [temp_list]])
    all_list.append(temp_list)
    unique_id += 1
    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        __walkData(child, level + 1, result_list, all_list, xpath)
    return


def getImageCfg(xml):
    level = 1  # 节点的深度从1开始
    result_list = []
    all_list = []
    # root = fromstring(xml).getroot()
    __walkData(fromstring(xml), level, result_list, all_list, '')
    for rlist in result_list:
        for columns in rlist[2]:
            if ('xUniqueKey' in columns[3]) and utils.valiXUniqueKey(columns[3]['xUniqueKey']):
                xUniqueCfg = utils.xUniqueKeyArray(columns[3]['xUniqueKey'])
                if 'u' == xUniqueCfg[0].lower():
                    num = columns[0] - xUniqueCfg[1]
                    columns[3][xUniqueCfg[3]] = str(all_list[num][3][xUniqueCfg[3]])
                else:
                    num = columns[0] + xUniqueCfg[1]
                    columns[3][xUniqueCfg[3]] = str(all_list[num][3][xUniqueCfg[3]])
    return result_list
