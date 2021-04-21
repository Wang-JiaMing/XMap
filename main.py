import xCore.xMapCore as xMapCore

import ImageData
import TestData


def print_hi():
    while (True):
        print(xMapCore.analXml(ImageData.xml, TestData.xml, {'xmlNamespace': 'urn:hl7-org:v3'}))

if __name__ == '__main__':
    print_hi()
