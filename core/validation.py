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
        # 判断
        if imageBaseInfo[1] == sourceBaseInfo[1] and imageBaseInfo[2] == sourceBaseInfo[2] and imageBaseInfo[4] == \
                sourceBaseInfo[4]:
            if 'xCheckKey' in imageBaseInfo[3]:
                _xCheckKey = imageBaseInfo[3]['xCheckKey']
                if imageBaseInfo[3][_xCheckKey] == sourceBaseInfo[3][_xCheckKey]:
                    existIndex = existIndex + 1
            else:
                existIndex = existIndex + 1
    if xCheck == '0..1' and existIndex > 1:
        return [False, '校验不通过，约束节点规范是0..1,实际节点存在' + str(existIndex) + ';校验路径:' + imageBaseInfo[4] + (
            '[' + imageBaseInfo[3]['xCheckKey'] + "=" + imageBaseInfo[3][
                imageBaseInfo[3]['xCheckKey']] + ']' if 'xCheckKey' in imageBaseInfo[3] else '')]
    if xCheck == '1..1' and existIndex != 1:
        return [False, '校验不通过，约束节点规范是1..1,实际节点存在' + str(existIndex) + ';校验路径:' + imageBaseInfo[4] + (
            '[' + imageBaseInfo[3]['xCheckKey'] + "=" + imageBaseInfo[3][
                imageBaseInfo[3]['xCheckKey']] + ']' if 'xCheckKey' in imageBaseInfo[3] else '')]
    if xCheck == '1..*' and existIndex < 1:
        return [False, '校验不通过，约束节点规范是1..*,实际节点存在' + str(existIndex) + ';校验路径:' + imageBaseInfo[4] + (
            '[' + imageBaseInfo[3]['xCheckKey'] + "=" + imageBaseInfo[3][
                imageBaseInfo[3]['xCheckKey']] + ']' if 'xCheckKey' in imageBaseInfo[3] else '')]
    return [True, '']
