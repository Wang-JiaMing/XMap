# -*- coding: utf-8 -*-
"""
    @Time 2020/10/28 23:47
    @Author wangjiaming
    @Version V0.1
    @File setup
    @Desc: pip库文件打包
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import setuptools
setup(
    name='XMap',  # 包的名字
    author='wangjiaming',  # 作者
    version='0.1.1',  # 版本号
    license='',

    description='analysis common xml',  # 描述
    long_description='''''',
    author_email='519677263@qq.com',  # 你的邮箱**
    url='',  # 可以写github上的地址，或者其他地址
    # 包内需要引用的文件夹
    # packages=setuptools.find_packages(exclude=['url2io',]),
    packages=["common","core","images","source",],
    # keywords='NLP,tokenizing,Chinese word segementation',
    # package_dir={'jieba':'jieba'},
    # package_data={'jieba':['*.*','finalseg/*','analyse/*','posseg/*']},

    # 依赖包
    install_requires=[],
    classifiers=[
        # 'Development Status :: 4 - Beta',
        # 'Operating System :: Microsoft'  # 你的操作系统  OS Independent      Microsoft
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: MIT License',
        # 'License :: OSI Approved :: BSD License',  # BSD认证
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3.7.3',  # python版本 。。。
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
)