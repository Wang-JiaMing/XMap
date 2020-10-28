# -*- coding: utf-8 -*-
"""
    @Time 2020/10/26 22:20
    @Author wangjiaming
    @Version V0.1
    @File XmlData
    @Desc:
"""
xml='''<?xml version="1.0" encoding="UTF-8"?>
<ClinicalDocument
    xmlns="urn:hl7-org:v3"
    xmlns:mif="urn:hl7-org:v3/mif"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 ..\sdschemas\SDA.xsd">
    <realmCode code="CN"></realmCode>
    <typeId root="2.16.840.1.113883.1.3" extension="POCD_MT000040"/>
    <templateId root="2.16.156.10011.2.1.1.21"/>
    <id root="2.16.156.10011.1.1" extension="9182323||1"/>
    <code code="C0001" codeSystem="2.16.156.10011.2.4" codeSystemName="卫生信息共享文档规范编码体系"/>
    <title>病历概要</title>
    <effectiveTime value="20190731162824"></effectiveTime>
    <confidentialityCode code="N" codeSystem="2.16.840.1.113883.5.25" codeSystemName="Confidentiality" displayName="正常访问保密级别"/>
    <languageCode code="zh-CN"></languageCode>
    <setId/>
    <versionNumber/>
    <!--文档记录对象（患者） [1..*] contextControlCode='OP' 表示本信息可以被重载-->
    <recordTarget typeCode="RCT" contextControlCode="OP">
        <patientRole classCode="PAT">
            <!--健康档案标识号-->
            <id root="2.16.156.10011.1.2" extension="00000000000557445"/>
            <!--健康卡号-->
            <id root="2.16.156.10011.1.19" extension="00000000000557445"/>
            <!--现住址-->
            <addr use="H">
                <houseNumber>-</houseNumber>
                <streetName>-</streetName>
                <township>-</township>
                <county>─</county>
                <city>娄底市</city>
                <state>湖南省</state>
                <postalCode>417000</postalCode>
            </addr>
            <telecom  value="13517427637"/>
            <patient classCode="PSN" determinerCode="INSTANCE">
                <!--患者身份证号-->
                <id root="2.16.156.10011.1.3" extension="432501193203070017"/>
                <name>袁吉良</name>
                <name>袁吉良1</name>

                <administrativeGenderCode code="1" codeSystem="2.16.156.10011.2.3.3.4" codeSystemName="生理性别代码表(GB/T 2261.1)" displayName="男性"/>
                <birthTime value="19320307" />
                <maritalStatusCode code="20" codeSystem="2.16.156.10011.2.3.3.5" codeSystemName="婚姻状况代码表(GB/T 2261.2)" displayName="已婚"/>
                <ethnicGroupCode code="01" codeSystem="2.16.156.10011.2.3.3.3" codeSystemName="民族类别代码表(GB 3304)" displayName="汉族"/>
                <!--工作单位-->
                <employerOrganization>
                    <name>无</name>
                    <telecom  value="13517427637"/>
                </employerOrganization>
                <!--职业状况-->
                <occupation>
                    <occupationCode code="90" codeSystem="2.16.156.10011.2.3.3.13" codeSystemName="从业状况(个人身体)代码表(GB/T 2261.4)" displayName="其他"/>
                </occupation>
            </patient>
        </patientRole>
    </recordTarget>
    <!--文档创作者-->
    <author typeCode="AUT" contextControlCode="OP">
        <time xsi:type="TS" value="20190510161920"/>
        <assignedAuthor classCode="ASSIGNED">
            <id root="2.16.156.10011.1.7" extension="864"/>
            <assignedPerson>
                <name>陈鹏亮</name>
            </assignedPerson>
            <representedOrganization>
                <id root="2.16.156.10011.1.5" extension="0187565656"/>
                <name>"南方医科大学南方医院"</name>
            </representedOrganization>
        </assignedAuthor>
    </author>
    <!--保管机构-->
    <custodian typeCode="CST">
        <assignedCustodian classCode="ASSIGNED">
            <representedCustodianOrganization classCode="ORG" determinerCode="INSTANCE">
                <id root="2.16.156.10011.1.5" extension="NFYKDXNFYY"/>
                <name>南方医科大学南方医院</name>
            </representedCustodianOrganization>
        </assignedCustodian>
    </custodian>
    <!--联系人-->
    <participant typeCode="NOT">
        <associatedEntity classCode="ECON">
            <!--联系人类别，表示与患者之间的关系-->
            <code code="2" codeSystem="2.16.156.10011.2.3.3.8" codeSystemName="家庭关系代码表" displayName="子"/>
            <!--联系人电话号码-->
            <telecom  use="H" value="13829993827"/>
            <!--联系人-->
            <associatedPerson classCode="PSN" determinerCode="INSTANCE">
                <!--联系人姓名-->
                <name>袁跃</name>
                <name>袁跃123</name>
            </associatedPerson>
        </associatedEntity>
    </participant>
    <participant typeCode="NOT">
        <associatedEntity classCode="ECON">
            <!--联系人类别，表示与患者之间的关系-->
            <code code="2" codeSystem="2.16.156.10011.2.3.3.8" codeSystemName="家庭关系代码表" displayName="子"/>
            <!--联系人电话号码-->
            <telecom  use="H" value="88888888888"/>
            <!--联系人-->
            <associatedPerson classCode="PSN" determinerCode="INSTANCE">
                <!--联系人姓名-->
                <name>袁12</name>
            </associatedPerson>
        </associatedEntity>
    </participant>
    <relatedDocument typeCode="RPLC">
        <parentDocument>
            <id/>
            <setId/>
            <versionNumber/>
        </parentDocument>
    </relatedDocument>
    <component>
        <structuredBody>
            <!--********************************************************实验室检查章节********************************************************-->
            <component>
                <section>
                    <code code="30954-2" displayName="STUDIES SUMMARY" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <!-- 血型-->
                    <entry typeCode="COMP">
                        <organizer classCode="BATTERY" moodCode="EVN">
                            <statusCode/>
                            <!-- ABO血型 -->
                            <component typeCode="COMP" contextConductionInd="true">
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE04.50.001.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
                                    <value xsi:type="CD" code="2" codeSystem="2.16.156.10011.2.3.1.85" codeSystemName="ABO血型代码表" displayName="B型"/>
                                </observation>
                            </component>
                            <!-- Rh血型 -->
                            <component typeCode="COMP" contextConductionInd="true">
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE04.50.010.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
                                    <value xsi:type="CD" code="2" codeSystem="2.16.156.10011.2.3.1.250" codeSystemName="Rh(D)血型代码表" displayName="阳性"/>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                </section>
            </component>
            <!--********************************************************既往史章节********************************************************-->
            <component>
                <section>
                    <code code="11348-0" displayName="HISTORY OF PAST ILLNESS" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <!-- 疾病史（含外伤） -->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.026.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="疾病史（含外伤）"/>
                            <value xsi:type="ST">“颈椎病”30余年；“痔疮”病史20余年；“膝关节痛”20年；“慢性支气管炎”22余年；“胃溃疡”10年，口服“奥美拉唑”治疗； 高血压病5年余，既往血压高压最高达200mmHg，曾因高血压致“鼻出血”，目前口服“络活喜”降压及“立普妥”降脂治疗，血压控制约130-140/70-80mmHg。2014年因“反复头晕”行头颅CT(2014-01-04，惠州市惠阳区人民医院)：1、右侧丘脑腔隙性梗塞（陈旧性）；2、脑萎缩，入我院，诊断“后循环缺血、脑白质变性、脑萎缩、脑动脉硬化”。否认肝炎、结核、传染病史，否认糖尿病、心脏病病史，20年前于当地医院行经尿道前列腺增生电切除术。否认其他重大手术、外伤史，无痢疾、疟疾、病毒性肝炎及结核等传染病史。预防接种史不详。无输血史,无药物过敏史。</value>
                        </observation>
                    </entry>
                    <!-- 传染病史 -->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.008.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="传染病史"/>
                            <value xsi:type="ST">无痢疾、疟疾、病毒性肝炎及结核等</value>
                        </observation>
                    </entry>
                    <!-- 手术史 -->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.026.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="手术史"/>
                            <value xsi:type="ST"></value>
                        </observation>
                    </entry>
                    <!--婚育史条目-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.098.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="婚育史"/>
                            <value xsi:type="ST">适龄结婚，配偶子女身体健康。</value>
                        </observation>
                    </entry>
                </section>
            </component>
            <!--********************************************************输血章节********************************************************-->
            <component>
                <section>
                    <code code="56836-0" displayName="History of blood transfusion" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <!-- 输血史 -->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.100.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="输血史"/>
                            <value xsi:type="ST">无</value>
                        </observation>
                    </entry>
                </section>
            </component>
            <!--********************************************************过敏史章节********************************************************-->
            <component>
                <section>
                    <code code="48765-2" displayName="Allergies, adverse reactions, alerts" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <!--过敏史条目-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.022.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="过敏史"/>
                            <value xsi:type="ST">无</value>
                        </observation>
                    </entry>
                </section>
            </component>
            <!--预防免疫史章节-->
            <component>
                <section>
                    <code code="11369-6" displayName="HISTORY OF IMMUNIZATIONS" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.100.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="预防接种史"/>
                            <value xsi:type="ST">预防接种史不详</value>
                        </observation>
                    </entry>
                </section>
            </component>
            <!--个人史章节-->
            <component>
                <section>
                    <code code="29762-2" displayName="Social history" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <!--个人史条目-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.097.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="个人史"/>
                            <value xsi:type="ST">生于湖南省娄底市，久居本地，无疫区、疫情、疫水接触史，营养中等，正力型发育，既往吸烟约20年，平均10支／日，已戒烟10余年。饮酒10余年，平均1两／日，已戒酒10余年。</value>
                        </observation>
                    </entry>
                </section>
            </component>
            <!--月经史章节-->
            <component>
                <section>
                    <code code="49033-4" displayName="Social history" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <!--月经史条目-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.102.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="月经史"/>
                            <value xsi:type="ST"></value>
                        </observation>
                    </entry>
                </section>
            </component>
            <!--家族史章节-->
            <component>
                <section>
                    <code code="10157-6" displayName="HISTORY OF FAMILY MEMBER DISEASES" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <!--家族史条目-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.10.103.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="家族史"/>
                            <value xsi:type="ST">父母健在，否认家族性遗传病史，否认家族性肿瘤病史。</value>
                        </observation>
                    </entry>
                </section>
            </component>
            <!-- 卫生事件章节 -->
            <component>
                <section>
                    <code  displayName="卫生事件"/>
                    <text/>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE08.10.026.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="医疗机构科室名称"/>
                            <value xsi:type="ST">南方医科大学南方医院</value>
                        </observation>
                    </entry>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.01.060.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="患者类型代码"/>
                            <value xsi:type="CD" code="3" codeSystem="2.16.156.10011.2.3.1.271" codeSystemName="患者类型代码表" displayName="住院"/>
                        </observation>
                    </entry>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE01.00.010.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="门（急）诊号"/>
                            <value xsi:type="ST">557445</value>
                        </observation>
                    </entry>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE01.00.014.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="住院号"/>
                            <value xsi:type="ST">557445</value>
                        </observation>
                    </entry>
                    <entry>
                        <organizer classCode="BATTERY" moodCode="EVN">
                            <statusCode/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE06.00.092.00" displayName="入院日期时间" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
                                    <value xsi:type="TS" value="20190510134403"/>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE06.00.017.00" displayName="出院日期时间" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
                                    <value xsi:type="TS" value="20190515075400"/>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE04.01.018.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="发病日期时间"/>
                            <value xsi:type="ST">20190510134403</value>
                        </observation>
                    </entry>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE05.10.053.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="就诊原因"/>
                            <effectiveTime value="20190510134403" />
                            <value xsi:type="ST">前尿道狭窄</value>
                        </observation>
                    </entry>
                    <!--条目：主要诊断-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE05.01.024.00" displayName="西医诊断编码" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录">
                                <qualifier>
                                    <name displayName="西医诊断编码" />
                                </qualifier>
                            </code>
                            <value xsi:type="CD" code="N35.900" codeSystem="2.16.156.10011.2.3.3.11" codeSystemName="ICD-10" displayName="前尿道狭窄"/>
                            <entryRelationship typeCode="COMP">
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE05.10.113.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="病情转归代码"/>
                                    <value xsi:type="CD" code="9" codeSystem="2.16.156.10011.2.3.1.148" codeSystemName="病情转归代码表" displayName="其他"/>
                                </observation>
                            </entryRelationship>
                        </observation>
                    </entry>
                    <!--条目：其他诊断-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE05.01.024.00" displayName="其他西医诊断编码" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录">
                                <qualifier>
                                    <name displayName="其他西医诊断编码" />
                                </qualifier>
                            </code>
                            <value xsi:type="CD" code="D30.400" codeSystem="2.16.156.10011.2.3.3.11" codeSystemName="ICD-10" displayName="尿道良性肿瘤"/>
                        </observation>
                    </entry>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE08.50.022.00" displayName="关键药物名称" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
                            <value xsi:type="ST">-</value>
                            <!-- 关键药物用法 -->
                            <entryRelationship typeCode="COMP">
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE05.10.113.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="关键药物用法"/>
                                    <value xsi:type="ST">-</value>
                                </observation>
                            </entryRelationship>
                            <!-- 药物不良反应情况 -->
                            <entryRelationship typeCode="COMP">
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE06.00.129.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="药物不良反应情况"/>
                                    <value xsi:type="ST">无</value>
                                </observation>
                            </entryRelationship>
                            <!-- 中药使用类别代码 -->
                            <entryRelationship typeCode="COMP">
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE06.00.129.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="中药使用类别代码"/>
                                    <value xsi:type="CD" code="1" codeSystem="2.16.156.10011.2.3.1.157" codeSystemName="中药使用类别代码表" displayName="未使用"/>
                                </observation>
                            </entryRelationship>
                        </observation>
                    </entry>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE06.00.251.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="其他医学处置"/>
                            <value xsi:type="ST">-</value>
                        </observation>
                    </entry>
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.01.039.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="责任医师姓名"/>
                            <value xsi:type="ST">陈鹏亮</value>
                        </observation>
                    </entry>
                    <!-- 费用条目 -->
                    <entry>
                        <organizer classCode="CLUSTER" moodCode="EVN">
                            <statusCode/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE02.01.044.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="医疗保险类别代码"/>
                                    <value xsi:type="CD" code="99" codeSystem="2.16.156.10011.2.3.1.248" codeSystemName="医疗保险类别代码表" displayName="其他"/>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE07.00.007.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="医疗付费方式代码"/>
                                    <value xsi:type="CD" code="08" codeSystem="2.16.156.10011.2.3.1.269" codeSystemName="医疗付费方式代码表" displayName="其他社会保险"/>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE07.00.007.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="门诊费用金额"/>
                                    <value xsi:type="MO" value="0.00" currency="元"/>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE07.00.010.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="住院费用金额"/>
                                    <value xsi:type="MO" value="11707.61" currency="元"/>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <code code="DE07.00.001.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="个人承担费用金额"/>
                                    <value xsi:type="MO" value="0.00" currency="元"/>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                </section>
            </component>
        </structuredBody>
    </component>
</ClinicalDocument>'''