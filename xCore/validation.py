# -*- coding: utf-8 -*-
"""
    @Time 2020/10/27 09:59
    @Author wangjiaming
    @Version V0.1
    @File valiXml
    @Desc:
"""
'''
    校验XML与镜像是否一样
'''
import logging
import xCommon.utils as utils

logging.getLogger().setLevel(logging.INFO)


def __valiCfg(cfg):
    if 'xmlNamespace' not in cfg:
        logging.error('配置缺失xmlNamespace');
        return False
    return True


def __valiSourceXML(imageBaseInfos, sourceBaseInfos):
    valiReuslts = []
    for imageBaseInfo in imageBaseInfos:
        if imageBaseInfo[0] != 'root':  # 根节点不校验
            for column in imageBaseInfo[2]:
                vr = __checkLen(column, sourceBaseInfos)
                if vr[0] == False:
                    valiReuslts.append(vr)
    return valiReuslts


# 校验约束
def __checkLen(imageBaseInfo, sourceBaseInfos):
    existIndex = 0
    xCheck = imageBaseInfo[3]['xCheck']
    for sourceBaseInfo in sourceBaseInfos:
        # 判断层级，节点和路径均为一样标签
        if imageBaseInfo[1] == sourceBaseInfo[1] and imageBaseInfo[2] == sourceBaseInfo[2] and imageBaseInfo[4] == \
                sourceBaseInfo[4]:
            if 'xUniqueKey' in imageBaseInfo[3]:
                xUniqueKey = imageBaseInfo[3]['xUniqueKey']  # 配置解析器
                if utils.valiXUniqueKey(xUniqueKey):
                    xUniqueKeyCfg = utils.xUniqueKeyArray(xUniqueKey)
                    if 'u' in xUniqueKeyCfg[0].lower():
                        # u 往上找
                        sourceNum = sourceBaseInfo[0] - xUniqueKeyCfg[1]
                        for sIndex in range(sourceNum, sourceBaseInfo[0]):
                            # 对比标签和属性是否都存在
                            if (utils.removeNameSpaces(sourceBaseInfos[sIndex][2].lower()) == xUniqueKeyCfg[2].lower()) and (
                                    xUniqueKeyCfg[3] in sourceBaseInfos[sIndex][3]):
                                # 是否有匹配上的值
                                if sourceBaseInfos[sIndex][3][xUniqueKeyCfg[3]] == imageBaseInfo[3][xUniqueKeyCfg[3]]:
                                    existIndex = existIndex + 1
                    else:
                        # d 往下找
                        sourceNum = sourceBaseInfo[0] + xUniqueKeyCfg[1]
                        for sIndex in range(sourceBaseInfo[0]+1, sourceNum+1):
                            if (utils.removeNameSpaces(sourceBaseInfos[sIndex][2].lower()) == xUniqueKeyCfg[2].lower()) and (
                                    xUniqueKeyCfg[3] in sourceBaseInfos[sIndex][3]):
                                if sourceBaseInfos[sIndex][3][xUniqueKeyCfg[3]] == imageBaseInfo[3][xUniqueKeyCfg[3]]:
                                    existIndex = existIndex + 1
                else:
                    # 直接对比标签和属性是否存在
                    if imageBaseInfo[3][xUniqueKey] == sourceBaseInfo[3][xUniqueKey] and (imageBaseInfo[3]['xValue']!='text' and valiParams(utils.getxValueKey(imageBaseInfo[3]['xValue']), sourceBaseInfo[3])):
                        existIndex = existIndex + 1
            else:
                existIndex = existIndex + 1
    valiStatus = True
    if xCheck == '0..1' and existIndex > 1:
        valiStatus=False
    if xCheck == '1..1' and existIndex != 1:
        valiStatus=False
    if xCheck == '1..*' and existIndex < 1:
        valiStatus=False
    if valiStatus==False:
        return [False, '校验不通过，约束节点规范是'+xCheck+',实际节点存在' + str(existIndex) + ';如果节点数据符合要求，关注节点取值是否有缺漏。校验路径:' + imageBaseInfo[4] + ('[' + (xUniqueKeyCfg[3] if utils.valiXUniqueKey(xUniqueKey) else xUniqueKey) + "=" + (imageBaseInfo[3][xUniqueKeyCfg[3]] if utils.valiXUniqueKey(xUniqueKey) else imageBaseInfo[3][xUniqueKey]) + ']' if 'xUniqueKey' in imageBaseInfo[3] else '')]
    return [True, '']


def valiParams(xValueArray,sourceParams):
    for xValue in xValueArray:
        if xValue not in sourceParams:
            return False
    return True