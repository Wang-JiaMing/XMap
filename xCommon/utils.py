# -*- coding: utf-8 -*-
"""
    @Time 2020/10/26 22:44
    @Author wangjiaming
    @Version V0.1
    @File Utils
    @Desc:
"""
import xCommon.parameter as param


def removeNameSpaces(str):
    return str.replace("{" + param.xmlNamespace + "}", '')


def resetXpath(root, str):
    return str.replace(root, "").replace("{" + param.xmlNamespace + "}", '')


def valiXUniqueKey(xUniqueKey):
    if xUniqueKey.find(":") != -1 and xUniqueKey.find('/'):
        return True
    return False


def findImageNode(imageBaseInfos, index):
    for imageBaseInfo in imageBaseInfos:
        for columns in imageBaseInfo[2]:
            if columns[0] == index:
                return columns
    return


def xUniqueKeyArray(xCheckKey):
    fstr = xCheckKey.split(":")
    str = fstr[1].split("/")
    return [fstr[0], len(str[0]), str[1], str[2]]


def getxValueKey(xValue):
    xValueArr = []
    xValueArray = xValue.split(";")
    for x in xValueArray:
        if 'z_' != x[0:2].lower():
            xValueArr.append(x)
    return xValueArr
