# -*- coding: utf-8 -*-
"""
    @Time 2020/10/26 22:20
    @Author wangjiaming
    @Version V0.1
    @File XmlData
    @Desc:
"""

# 南方
xml='''<?xml version="1.0" encoding="utf-8"?>

<ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:mif="urn:hl7-org:v3/mif" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 file:///D:/HTP/CDACoreSchemas/sdschemas/CDA.xsd">
  <realmCode code="CN"/>
  <typeId root="2.16.840.1.113883.1.3" extension="POCD_MT000040"/>
  <templateId root="2.16.156.10011.2.1.1.43"/>
  <id root="2.16.156.10011.1.1" extension="RN001"/>
  <code code="C0023" codeSystem="2.16.156.10011.2.4" codeSystemName="卫生信息共享文档规范编码体系"/>
  <title>入院评估</title>
  <effectiveTime value="20191112033728"/>
  <confidentialityCode code="N" displayName="正常访问保密级别" codeSystem="2.16.840.1.113883.5.25" codeSystemName="Confidentiality"/>
  <languageCode code="zh-CN"/>
  <setId/>
  <versionNumber/>
  <recordTarget typeCode="RCT" contextControlCode="OP">
    <patientRole classCode="PAT">
      <id root="2.16.156.10011.1.19" extension="440125196103283747"/>
      <id root="2.16.156.10011.1.12" extension="1042353"/>
      <telecom use="MP" value="15917379263"/>
      <telecom use="WP" value="-"/>
      <telecom use="EM" value=""/>
      <patient classCode="PSN" determinerCode="INSTANCE">
        <id root="2.16.156.10011.1.3" extension="440125196103283747"/>
        <name>李秀莲</name>
        <administrativeGenderCode code="2" displayName="女性" codeSystem="2.16.156.10011.2.3.3.4" codeSystemName="生理性别代码表(GB/T 2261.1)"/>
        <maritalStatusCode code="20" displayName="已婚" codeSystem="2.16.156.10011.2.3.3.5" codeSystemName="婚姻状况代码表(GB/T 2261.2)"/>
        <ethnicGroupCode code="01" displayName="汉族" codeSystem="2.16.156.10011.2.3.3.3" codeSystemName="民族类别代码表(GB 3304)"/>
        <nationality code="156" codeSystem="2.16.156.10011.2.3.3.1" codeSystemName="世界各国和地区名称代码(GB/T 2659)" displayName="中国"/>
        <age unit="岁" value="58"/>
        <educationLevel>
          <educationLevelCode code="90" displayName="其他" codeSystem="2.16.156.10011.2.3.3.6" codeSystemName="学历代码表(GB/T 4658)"/>
        </educationLevel>
        <occupation>
          <occupationCode code="70" displayName="无业人员" codeSystem="2.16.156.10011.2.3.3.13" codeSystemName="从业状况(个人身体)代码表(GB/T 2261.4)"/>
        </occupation>
      </patient>
    </patientRole>
  </recordTarget>
  <author typeCode="AUT" contextControlCode="OP">
    <time value="201905071029"/>
    <assignedAuthor classCode="ASSIGNED">
      <id root="2.16.156.10011.1.7" extension="NLYY1"/>
      <assignedPerson>
        <name>刘莹莹</name>
      </assignedPerson>
    </assignedAuthor>
  </author>
  <custodian typeCode="CST">
    <assignedCustodian classCode="ASSIGNED">
      <representedCustodianOrganization classCode="ORG" determinerCode="INSTANCE">
        <id root="2.16.156.10011.1.5" extension="NFYKDXNFYY"/>
        <name>南方医科大学南方医院</name>
      </representedCustodianOrganization>
    </assignedCustodian>
  </custodian>
  <legalAuthenticator typeCode="LA">
    <time value="20190507102900"/>
    <signatureCode/>
    <assignedEntity>
      <id root="2.16.156.10011.1.4" extension="WCX"/>
      <code displayName="责任护士"/>
      <assignedPerson>
        <name>邬朝星</name>
      </assignedPerson>
    </assignedEntity>
  </legalAuthenticator>
  <authenticator>
    <time value="20190507102900"/>
    <signatureCode/>
    <assignedEntity classCode="ASSIGNED">
      <id root="2.16.156.10011.1.4" extension="NLYY1"/>
      <code displayName="接诊护士"/>
      <assignedPerson classCode="PSN">
        <name>刘莹莹</name>
      </assignedPerson>
    </assignedEntity>
  </authenticator>
  <participant typeCode="NOT">
    <associatedEntity classCode="ECON">
      <code/>
      <telecom value="-"/>
      <associatedPerson>
        <name>-</name>
      </associatedPerson>
    </associatedEntity>
  </participant>
  <componentOf typeCode="COMP">
    <encompassingEncounter classCode="ENC" moodCode="EVN">
      <code/>
      <effectiveTime nullFlavor="NI"/>
      <location typeCode="LOC">
        <healthCareFacility classCode="SDLOC">
          <serviceProviderOrganization classCode="ORG" determinerCode="INSTANCE">
            <asOrganizationPartOf classCode="PART">
              <wholeOrganization classCode="ORG" determinerCode="INSTANCE">
                <id root="2.16.156.10011.1.22" extension="71"/>
                <name>71</name>
                <asOrganizationPartOf classCode="PART">
                  <wholeOrganization classCode="ORG" determinerCode="INSTANCE">
                    <id root="2.16.156.10011.1.21" extension="1018"/>
                    <name>1018</name>
                    <asOrganizationPartOf classCode="PART">
                      <wholeOrganization classCode="ORG" determinerCode="INSTANCE">
                        <id root="2.16.156.10011.1.27" extension="H210102"/>
                        <name>XXGNKHLDY-心血管内科护理单元</name>
                        <asOrganizationPartOf classCode="PART">
                          <wholeOrganization classCode="ORG" determinerCode="INSTANCE">
                            <id root="2.16.156.10011.1.26" extension="210102"/>
                            <name>XXGNKBF-心血管内科病房</name>
                            <asOrganizationPartOf classCode="PART">
                              <wholeOrganization classCode="ORG" determinerCode="INSTANCE">
                                <id root="2.16.156.10011.1.5" extension="NFYKDXNFYY"/>
                                <name>南方医科大学南方医院</name>
                              </wholeOrganization>
                            </asOrganizationPartOf>
                          </wholeOrganization>
                        </asOrganizationPartOf>
                      </wholeOrganization>
                    </asOrganizationPartOf>
                  </wholeOrganization>
                </asOrganizationPartOf>
              </wholeOrganization>
            </asOrganizationPartOf>
          </serviceProviderOrganization>
        </healthCareFacility>
      </location>
    </encompassingEncounter>
  </componentOf>
  <component>
    <structuredBody>
      <component>
        <section>
          <code displayName="入院信息"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.053.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="入院原因"/>
              <value xsi:type="ST">胸闷、气促1年余，加重伴咳嗽、咳痰1天。</value>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE06.00.339.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="入院途径代码"/>
              <value xsi:type="CD" code="1" displayName="门诊" codeSystem="2.16.156.10011.2.3.1.270" codeSystemName="入院途径代码表"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE06.00.237.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="入病房方式"/>
              <value xsi:type="ST">步行</value>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code code="11450-4" displayName="PROBLEM LIST" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE04.01.118.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="主要症状名称"/>
              <value xsi:type="ST">房间隔缺损（继发孔型）</value>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code code="8716-3" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="VITAL SIGNS"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE04.10.186.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="体温(℃)"/>
              <value xsi:type="PQ" value="36.5" unit="℃"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE04.10.118.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="脉率"/>
              <value xsi:type="PQ" value="89" unit="次/min"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE04.10.081.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="呼吸频率"/>
              <value xsi:type="PQ" value="15" unit="次/min"/>
            </observation>
          </entry>
          <entry>
            <organizer classCode="BATTERY" moodCode="EVN">
              <statusCode/>
              <component>
                <observation classCode="OBS" moodCode="EVN">
                  <code code="DE04.10.174.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="收缩压"/>
                  <value xsi:type="PQ" value="170" unit="mmHg"/>
                </observation>
              </component>
              <component>
                <observation classCode="OBS" moodCode="EVN">
                  <code code="DE04.10.176.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="舒张压"/>
                  <value xsi:type="PQ" value="99" unit="mmHg"/>
                </observation>
              </component>
            </organizer>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE04.10.188.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="体重"/>
              <value xsi:type="PQ" value="57.00" unit="kg"/>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code code="11348-0" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="HISTORY OF PAST ILLNESS"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE02.10.026.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="疾病史(含外伤)"/>
              <value xsi:type="ST">无手术史</value>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE02.10.008.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="传染病史"/>
              <value xsi:type="ST">无痢疾、疟疾、病毒性肝炎及结核等</value>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE02.10.101.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="预防接种史"/>
              <value xsi:type="ST">预防接种史不详</value>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE02.10.061.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="手术史"/>
              <value xsi:type="ST">手术史</value>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE02.10.100.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="输血史"/>
              <value xsi:type="ST">无</value>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.031.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="一般健康状况标志"/>
              <value xsi:type="BL" value="true"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.119.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="患者传染性标志"/>
              <value xsi:type="BL" value="false"/>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code code="48765-2" displayName="Allergies, adverse reactions, alerts" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE02.10.022.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="过敏史"/>
              <value xsi:type="ST">无</value>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code code="10157-6" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="HISTORY OF FAMILY MEMBER DISEASES"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE02.10.103.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="家族史"/>
              <value xsi:type="ST">母亲有高血压病史，否认家族性遗传病史，否认家族性肿瘤病史。</value>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code code="51848-0" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="Assessment note"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.001.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="Apgar评分值"/>
              <value xsi:type="INT" value="0"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.022.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="发育程度代码"/>
              <value xsi:type="CD" code="1" displayName="正力型" codeSystem="2.16.156.10011.2.3.2.53" codeSystemName="发育程度代码表"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.142.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="精神状态正常标志"/>
              <value xsi:type="BL" value="true"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.065.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="睡眠状况"/>
              <value xsi:type="ST">正常</value>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.158.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="特殊情况"/>
              <value xsi:type="ST">详见护理单。</value>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.084.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="心理状态代码"/>
              <value xsi:type="CD" code="9" displayName="其他" codeSystem="2.16.156.10011.2.3.1.140" codeSystemName="心理状态代码表"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.097.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="营养状态代码"/>
              <value xsi:type="CD" code="1" displayName="良好" codeSystem="2.16.156.10011.2.3.2.54" codeSystemName="营养状态代码表"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.122.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="自理能力代码"/>
              <value xsi:type="CD" code="1" displayName="完全自理" codeSystem="2.16.156.10011.2.3.2.55" codeSystemName="自理能力代码表"/>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code displayName="生活方式"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE03.00.070.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="吸烟标志"/>
              <value xsi:type="BL" value="false"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE03.00.073.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="吸烟状况代码"/>
              <value xsi:type="CD" code="1" displayName="从不吸烟" codeSystem="2.16.156.10011.2.3.2.5" codeSystemName="吸烟状况代码表"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE03.00.053.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="日吸烟量(支)"/>
              <value xsi:type="PQ" value="0" unit="支"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE03.00.065.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="停止吸烟天数"/>
              <value xsi:type="PQ" value="0" unit="d"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE03.00.030.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="饮酒标志"/>
              <value xsi:type="BL" value="false"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE03.00.076.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="饮酒频率代码"/>
              <value xsi:type="CD" code="1" displayName="从不" codeSystem="2.16.156.10011.2.3.1.16" codeSystemName="饮酒频率代码表"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE03.00.054.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="日饮酒量（mL）"/>
              <value xsi:type="PQ" value="0" unit="mL"/>
            </observation>
          </entry>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE03.00.080.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="饮食情况代码"/>
              <value xsi:type="CD" code="1" displayName="良好" codeSystem="2.16.156.10011.2.3.2.34" codeSystemName="饮食情况代码表"/>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code code="46241-6" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="HOSPITAL ADMISSION DX"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.01.024.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="入院诊断编码"/>
              <value xsi:type="CD" code="Q21.102" displayName="房间隔缺损（继发孔型）" codeSystem="2.16.156.10011.2.3.3.11" codeSystemName="ICD-10"/>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code displayName="护理观察"/>
          <text/>
          <entry>
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE02.10.031.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="护理观察项目名称"/>
              <value xsi:type="ST">-</value>
              <entryRelationship typeCode="COMP">
                <observation classCode="OBS" moodCode="EVN">
                  <code code="DE02.10.028.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="护理观察结果"/>
                  <value xsi:type="ST">-</value>
                </observation>
              </entryRelationship>
            </observation>
          </entry>
        </section>
      </component>
      <component>
        <section>
          <code code="8648-8" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="Hospital Course"/>
          <text/>
          <entry typeCode="COMP">
            <observation classCode="OBS" moodCode="EVN">
              <code code="DE05.10.144.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="评估日期时间"/>
              <value xsi:type="TS" value="201905071029"/>
            </observation>
          </entry>
        </section>
      </component>
    </structuredBody>
  </component>
</ClinicalDocument>

'''