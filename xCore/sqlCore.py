# -*- coding: utf-8 -*-
"""
    @Time 2020/10/27 12:55
    @Author wangjiaming
    @Version V0.1
    @File SqlCore
    @Desc:
"""
import xCommon.utils as utils


#    '错误日志sql'
def __errSql(vailResult):
    sql = []
    for vali in vailResult:
        sqlStr = "insert into TB_CDA_ERR_LOG(source_id, error_msg) values(z_source_id,'" + utils.removeNameSpaces(str(vali[1]).replace('\'', '')) + "')"
        sql.append(sqlStr)
    return sql


def __getOneTableSql(oneSqlParams):
    sql = []
    for tableList in oneSqlParams:
        feilds = ''
        values = ''
        for feild in tableList[1]:
            feilds = ('' if feilds == '' else feilds + ',') + feild[0]
            values = ('' if values == '' else values + ',') + "'" + feild[1] + "'"
        sql.append('insert into ' + tableList[0].upper() + "(" + feilds.upper() + ")values(" + values + ")")
    return sql


def __getMaynTableSql(maySqlParams):
    sql = []
    for table in maySqlParams:
        feilds = ''
        values = ''
        for fav in table[2]:
            feilds = ('' if feilds == '' else feilds + ',') + fav[0]
            values = ('' if values == '' else values + ',') + "'" + fav[1].replace(',', ';') + "'"
        sql.append('insert into ' + table[1].upper() + "(" + feilds.upper() + ")values(" + values + ")")
    return sql
