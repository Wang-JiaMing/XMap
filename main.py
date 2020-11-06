import xCore.xMapCore as xMapCore

import TestP4Data
import XmlP4Data
import TestData
import XmlData


def print_hi():
      print(xMapCore.analXml(XmlData.xml, TestData.xml, {'xmlNamespace': 'urn:hl7-org:v3'}))
     # print(xMapCore.autoCreateTable(XmlP4Data.xml, {'xmlNamespace': 'urn:hl7-org:v3','expColumns':'ID               VARCHAR2(32) default sys_guid() not null primary key,\
     # REMOVED          VARCHAR2(1)  default 0,\
     # CREATED_BY       VARCHAR2(100),\
     # CREATED_TIME     DATE         default sysdate,\
     # UPDATED_BY       VARCHAR2(100),\
     # UPDATED_TIME     DATE,'}))
    # for r in xMapCore.analXml(XmlData.xml,TestData.xml):
    # for ri in r:
    # print(ri)


if __name__ == '__main__':
    print_hi()
