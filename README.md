# XML镜像解析器(XMap)
```
    author：wangjiaming
    createDate：20201026
```
    
## 一、序言
- 本软件是解析xml的通用方案，通过配置镜像xml，再重组镜像xml和源xml的数据，
对源xml进行镜像化解析。最终以插入语句方式输出。程序目前分为两大功能点：
1. `通过镜像Xml和源Xml进行镜像化解析，从而获取插入语句`
2. `通过镜像Xml生产建表语句`

## 二、核心解析器(镜像化解析)

### 2.1 调用方法
    xMapCore.analXml(ImageXml, SourceXml, {'xmlNamespace': 'urn:hl7-org:v3'})
1. ImageXml：`镜像xml字符串`
2. SourceXml：`源xml字符串`
3. {'xmlNamespace': 'urn:hl7-org:v3'}：`配置参数`
    - 目前暂只支持xmlNamespace(命名空间配置)
   
### 2.2 回参
参考第四章节回参

### 2.3 镜像Xml配置属性(*`重点`*)
1.  xCheck  `必填[值域：0..1、0..*、1..1、1..*]`

    只有存在xCheck的属性的xml才被扫描到，如果该属性下的xTable没携带xLooDots或者xLooDots=False，即0..\*或者1..\*,存在多个值情况下，会以`;`分割

2. xUniqueKey `非必填`

    `xCheckKey更名为xUniqueKey`,唯一定位字段，用来定位与数据来源放进行校验；
    相对路径查找方法：
- 例子：u:../code/code
- 解析：查询方向:层级/标签/属性名
    - 查询方向：
        - u:往上查找
        - d:往下查询
    - 层级:
        - 一个小点代表一层
    - 标签:xml标签名
    - 属性名:xml标签下的属性
3. xTable   `必填`
        
    值对应写入的表名
    
4. xKey `非必填`
        
    允许不存在，如果该属性不存在，字段名以xml标签为准，如果多个值用`;`分割,**`分割量必须与xValue分割量一致`**
   
5. xValue   `必填`
   
    取值位置,如果需设置为占位符，即以"z_"开头即可。例如："z_id"；如果多个值用`;`分割,**`分割量必须与xKey分割量一致`**

6. xLoopDots    `非必填[值域：True（循环），False（不循环）]`

    循环点，xLopDots节点上的xKey、和xValue将会失效，如需要添加占位符字段，可以在循环体内寻找存在xCheck属性的标签进行添加。
        

### 2.4 xml重装配置数组定义
1. 镜像重组配置
```
imageBaseInfo=
[
    tableName,
    loopType,
    [unique_id, level, root_node.tag, root_node.attrib, xpath]
]
```
        
    tableName：表名
    loopType：是否为循环点，值域：-、loopDot【-否；loopDot是】
    unique_id：序号
    level：树层级
    root_node.tag：标签
    root_node.attrib：属性
    xpath：标签路径

2.源xml重组配置

```
sourceBaseInfo=
[
        unique_id, 
        level, 
        root_node.tag, 
        root_node.attrib, 
        xpath,source_id,
        text
]
```
    
     
    unique_id：序号
    level：树层级
    root_node.tag：标签
    root_node.attrib：属性
    xpath：标签路径
    source_id：数据来源唯一编码
    text：标签对的值

## 三、自动化建表
### 3.1 调用方法
    xMapCore.autoCreateTable(ImageData, {'xmlNamespace': 'urn:hl7-org:v3'})
1. ImageData：`镜像xml字符串`
3. {'xmlNamespace': 'urn:hl7-org:v3'}：`配置参数`
- 目前暂支持参数有：
    - xmlNamespace:''   (命名空间配置，`必填`)
    - expColumns:['ID               VARCHAR2(32) default sys_guid() not null primary key,
    REMOVED          VARCHAR2(1)  default 0,
    CREATED_BY       VARCHAR2(100),
    CREATED_TIME     DATE         default sysdate,
    UPDATED_BY       VARCHAR2(100),
    UPDATED_TIME     DATE,'] 扩展建表语句
### 3.2 回参
参考第四章节回参

## 四、SQL回参
所有回参结果以一维数组方式反馈，数据里存放0..*个SQL语句。例：
```sql
["insert into TB_CDA_ERR_LOG(source_id, error_msg)
values (z_source_id,
        '校验不通过，约束节点规范是1..1,实际节点存在0;校验路径:/{urn:hl7-org:v3}ClinicalDocument/{urn:hl7-org:v3}recordTarget/{urn:hl7-org:v3}patientRole/{urn:hl7-org:v3}id[root=2.16.156.10011.1.19]')]"

```

## 五、安装方式
首先本地开发环境需要pip环境，通过pip对本地化tar.gz文件进行，命令如下:
```
    pip install %XMap_HOME%/Xmap-0.1.tar.gz
```
