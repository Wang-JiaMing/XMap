# -*- coding: utf-8 -*-
"""
    @Time 2020/10/26 23:22
    @Author wangjiaming
    @Version V0.1
    @File valiXml
    @Desc:校验镜像xml与来源xml是否都存在该有的节点
"""
import xCore.validation as vali
import xCore.sqlCore as sqlCore
import xImages.baseInfo as ibaseInfo
import xSource.baseInfo as sbaseInfo
import xCommon.utils as utils
import xCommon.parameter as parameter
import time


# 解析XML主入口
def analXml(imageXml, sourceXml, cfg):
    ibaseInfo.unique_id = 0
    sbaseInfo.unique_id = 0

    beginTime = time.time()
    if vali.__valiCfg(cfg) == False:
        return sqlCore.__errSql([False, 'cfg配置参数错误'])
    parameter.xmlNamespace = cfg['xmlNamespace']
    imageBaseInfos = ibaseInfo.getImageCfg(imageXml)
    sourceBaseInfos = sbaseInfo.getSourceXmlCfg(sourceXml)
    sql = __core(imageBaseInfos, sourceBaseInfos)
    print("处理完成！一共生产【" + str(len(sql)) + "】条SQL数据，耗时：" + str(int(round((time.time() - beginTime) * 1000))) + 'ms')
    return sql


def autoCreateTable(imageXml, cfg):
    sql = []
    beginTime = time.time()
    if vali.__valiCfg(cfg) == False:
        return sqlCore.__errSql([False, 'cfg配置参数错误'])
    imageBaseInfos = ibaseInfo.getImageCfg(imageXml)
    for imageXml in imageBaseInfos:
        if 'root' != imageXml[0]:
            createStr = "create table " + imageXml[0] + "("
            if 'expColumns' in cfg:
                createStr = createStr + cfg['expColumns']
            for columnsIndex in range(0, len(imageXml[2])):
                if 'xKey' not in imageXml[2][columnsIndex][3]:
                    createStr = createStr + utils.removeNameSpaces(imageXml[1]) + ' varchar2(50),'
                else:
                    for xKeyIndex in range(0, len((imageXml[2][columnsIndex][3]['xKey']).split(';'))):
                        createStr = createStr + (imageXml[2][columnsIndex][3]['xKey']).split(';')[
                            xKeyIndex] + ' varchar2(50),'
            createStr = createStr[0:len(createStr) - 1] + ")"
            sql.append(createStr.upper())
    print("处理完成！一共生产【" + str(len(sql)) + "】条SQL数据，耗时：" + str(int(round((time.time() - beginTime) * 1000))) + 'ms')
    return sql


# 核心解析器
def __core(imageBaseInfos, sourceBaseInfos):
    vailResult = vali.__valiSourceXML(imageBaseInfos, sourceBaseInfos)
    if len(vailResult) > 0:
        return sqlCore.__errSql(vailResult)
    else:
        return __analysisTable(imageBaseInfos, sourceBaseInfos)


# 分析表
def __analysisTable(imageBaseInfos, sourceBaseInfos):
    allSql = []
    for images in imageBaseInfos:
        if images[0] != 'root' and images[1] == '-':
            for sqli in sqlCore.__getOneTableSql(__oneTable(images, sourceBaseInfos)):
                allSql.append(sqli)
        elif images[0] != 'root' and images[1] == 'loopDot':
            for sqli in sqlCore.__getMaynTableSql(__manyTable(images, sourceBaseInfos)):
                allSql.append(sqli)
    return allSql


# 单表解析
def __oneTable(imageBaseInfos, sourceBaseInfos):
    tableParams = []
    for imageBaseInfo in imageBaseInfos[2]:
        for r in __getSourceBaseInfos(imageBaseInfo, sourceBaseInfos):
            vx = imageBaseInfo[3]['xValue'].split(';')
            for index in range(0, len(vx)):
                tableName = imageBaseInfo[3]['xTable']
                field = (utils.removeNameSpaces(imageBaseInfo[2]) if 'xKey' not in imageBaseInfo[3] else
                         imageBaseInfo[3]['xKey'].split(';')[index])
                if 'text' != imageBaseInfo[3]['xValue'].split(';')[index] and 'z_' != \
                        imageBaseInfo[3]['xValue'].split(';')[index][0:2]:
                    if imageBaseInfo[3]['xValue'].split(';')[index] in r[3]:
                        xValue = r[3][vx[index]]
                    else:
                        xValue = ''
                elif 'z_' != imageBaseInfo[3]['xValue'].split(';')[index][0:2]:
                    xValue = r[5]
                else:
                    xValue = vx[index]
                tableArray = [field, xValue]
                inTableStatus = True
                for oTable in tableParams:
                    # 判断表是否已存在
                    if tableName == oTable[0]:
                        inTableStatus = False
                        _field_status = True
                        for _field in oTable[1]:
                            if _field[0] == field:
                                _field[1] = _field[1] + ";" + xValue
                                _field_status = False
                                break
                        if _field_status:
                            oTable[1].append(tableArray)
                        break
                if inTableStatus:
                    tableParams.append([imageBaseInfo[3]['xTable'], [tableArray]])
    return tableParams


# 多表解析
def __manyTable(imageBaseInfos, sourceBaseInfos):
    tableParams = []  # [index,tableName,[field,value]]
    loopDots = __getSourceBaseInfos(imageBaseInfos[2][0], sourceBaseInfos)  # 获取循环点数量

    # 遍历镜像所有循环节点标签
    for index in range(0, len(loopDots)):

        for imageBaseInfo in imageBaseInfos[2]:
            for sourceBaseInfo in __getSourceBaseInfos(imageBaseInfo, sourceBaseInfos):
                if index < len(loopDots) - 1:  # 有后继节点
                    if sourceBaseInfo[0] > loopDots[index][0] and sourceBaseInfo[0] < loopDots[index + 1][0]:
                        __manyTableArray(index, imageBaseInfo, sourceBaseInfo, tableParams)
                else:  # 最后一个节点
                    if sourceBaseInfo[0] > loopDots[index][0]:
                        __manyTableArray(index, imageBaseInfo, sourceBaseInfo, tableParams)
    return tableParams


# 多表数组
def __manyTableArray(index, imageBaseInfo, sourceBaseInfo, tableParams):
    vx = imageBaseInfo[3]['xValue'].split(';')
    for vxIndex in range(0, len(vx)):
        tableName = imageBaseInfo[3]['xTable']
        field = (utils.removeNameSpaces(imageBaseInfo[2]) if 'xKey' not in imageBaseInfo[3] else
                 imageBaseInfo[3]['xKey'].split(';')[vxIndex])
        if 'text' != imageBaseInfo[3]['xValue'].split(';')[vxIndex] and 'z_' != imageBaseInfo[3]['xValue'].split(';')[
                                                                                    vxIndex][0:2]:
            xValue = sourceBaseInfo[3][vx[vxIndex]]
        elif 'z_' != imageBaseInfo[3]['xValue'].split(';')[vxIndex][0:2]:
            xValue = sourceBaseInfo[5]
        else:
            xValue = vx[vxIndex]
        tableArray = [field, xValue]
        inTableStatus = True
        for oTable in tableParams:
            # 判断表是否已存在
            if tableName == oTable[1] and index == oTable[0]:
                inTableStatus = False
                # 判断字段是否已经存在
                _field_status = True
                for _field in oTable[2]:
                    if _field[0] == field:
                        _field[1] = _field[1] + ";" + xValue
                        _field_status = False
                        break
                if _field_status:
                    oTable[2].append(tableArray)
                break
        if inTableStatus:
            tableParams.append([index, imageBaseInfo[3]['xTable'], [tableArray]])


# 获取baseInfo
def __getSourceBaseInfos(imageBaseInfo, sourceBaseInfos):
    sBaseInfos = []
    for sourceBaseInfo in sourceBaseInfos:
        # 判断
        if imageBaseInfo[1] == sourceBaseInfo[1] and imageBaseInfo[2] == sourceBaseInfo[2] and imageBaseInfo[4] == \
                sourceBaseInfo[4]:
            if 'xUniqueKey' in imageBaseInfo[3]:
                if utils.valiXUniqueKey(imageBaseInfo[3]['xUniqueKey']):
                    # 语法定位
                    _xUniqueKey = utils.xUniqueKeyArray(imageBaseInfo[3]['xUniqueKey'])
                    if 'u' == _xUniqueKey[0]:  # 上
                        sourceNum = sourceBaseInfo[0] - _xUniqueKey[1]
                        for sIndex in range(sourceNum, sourceBaseInfo[0]):
                            if (utils.removeNameSpaces(sourceBaseInfos[sIndex][2].lower()) == _xUniqueKey[
                                2].lower()) and (
                                    _xUniqueKey[3] in sourceBaseInfos[sIndex][3]):
                                # 是否有匹配上的值
                                if sourceBaseInfos[sIndex][3][_xUniqueKey[3]] == imageBaseInfo[3][_xUniqueKey[3]]:
                                    sBaseInfos.append(sourceBaseInfo)

                    else:  # 下
                        sourceNum = sourceBaseInfo[0] + _xUniqueKey[1]
                        for sIndex in range(sourceBaseInfo[0]+1, sourceNum+1):
                            if (utils.removeNameSpaces(sourceBaseInfos[sIndex][2].lower()) == _xUniqueKey[2].lower()) and (
                                    _xUniqueKey[3] in sourceBaseInfos[sIndex][3]):
                                if sourceBaseInfos[sIndex][3][_xUniqueKey[3]] == imageBaseInfo[3][_xUniqueKey[3]]:
                                    sBaseInfos.append(sourceBaseInfo)

                else:
                    # 非语法定位
                    if imageBaseInfo[3][imageBaseInfo[3]['xUniqueKey']] == sourceBaseInfo[3][
                        imageBaseInfo[3]['xUniqueKey']]:
                        sBaseInfos.append(sourceBaseInfo)
            else:
                sBaseInfos.append(sourceBaseInfo)
    return sBaseInfos
