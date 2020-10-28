#XML地图(XMap)
    author：wangjiaming
    createDate：20201026
## 序言
        本软件是解析xml的通用方案，通过配置镜像xml，再重组镜像xml和源xml的数据，
    对源xml进行镜像化解析。最终以insert语句方式输出。

## xml重装配置数组定义
    1.镜像重组配置
    imageBaseInfo=[
        tableName,
        loopType,
        [unique_id, level, root_node.tag, root_node.attrib, xpath]
        ]
        
    tableName：表名
    loopType：是否为循环点，值域：-、loopDot【-否；loopDot是】
    unique_id：序号
    level：树层级
    root_node.tag：标签
    root_node.attrib：属性
    xpath：标签路径
    
    2.源xml重组配置
    sourceBaseInfo=[
        unique_id, 
        level, 
        root_node.tag, 
        root_node.attrib, 
        xpath,source_id,
        text
        ]
       
    unique_id：序号
    level：树层级
    root_node.tag：标签
    root_node.attrib：属性
    xpath：标签路径
    source_id：数据来源唯一编码
    text：标签对的值

## 镜像配置属性
    1.  xCheck
        **必填**
        只有存在xCheck的属性的xml才被扫描到，如果该属性下的xTable没携带xLooDots或者xLooDots=False，即0..*或者1..*,存在多个值情况下，
        会以';'分割
        值域：0..1、0..*、1..1、1..*
    2. xCheckKey
        获取镜像校验字段，用来定位与数据来源放进行校验
    2. xTable
        **必填**
        值对应写入的表名
    3. xKey
        允许不存在，如果该属性不存在，字段名以xml标签为准，如果多个值用';'分割,分割量必须与xValue一致
    4. xValue
        **必填**
        取值位置,如果需设置为占位符，即以"z_"开头即可。例如："z_id"；如果多个值用';'分割,分割量必须与xKey一致
    5. xLoopDots
        循环点
        值域：True（循环），False（不循环）
        xLoopDots节点上的xKey、和xValue将会失效，如需要添加占位符字段，可以在循环体内进行添加
        
       
    
## SQL回参
#### 错误日志SQL
    若果校验不通过，将会短路返回错误日志插入语句，其中z_source_id需要替换成自己的变量，例如：
```sql
insert into TB_CDA_ERR_LOG(source_id, error_msg)
values (z_source_id,
        '校验不通过，约束节点规范是1..1,实际节点存在0;校验路径:/{urn:hl7-org:v3}ClinicalDocument/{urn:hl7-org:v3}recordTarget/{urn:hl7-org:v3}patientRole/{urn:hl7-org:v3}id[root=2.16.156.10011.1.19]')
```
    
