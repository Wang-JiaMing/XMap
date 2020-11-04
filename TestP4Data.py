# -*- coding: utf-8 -*-
"""
    @Time 2020/10/29 16:00
    @Author wangjiaming
    @Version V0.1
    @File TestP4Data
    @Desc:
"""
xml='''<?xml version="1.0" encoding="UTF-8"?>
<ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:mif="urn:hl7-org:v3/mif" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 ..\sdschemas\CDA.xsd">
	<realmCode code="CN"/>
	<typeId root="2.16.840.1.113883.1.3" extension="POCD_MT000040"/>
	<templateId  root="2.16.156.10011.2.1.1.24"/>
	
	<!-- 文档流水号 -->
	<id root="2.16.156.10011.1.1" extension="0000EE2081710391625"/>
	
	<code code="C0004" codeSystem="2.16.156.10011.2.4" codeSystemName="卫生信息共享文档规范编码体系"></code>
	<title>西药处方</title>
	
	<!-- 文档机器生成时间 -->
	<effectiveTime value="20200817103901"/>
	<confidentialityCode code="N" codeSystem="2.16.840.1.113883.5.25" codeSystemName="Confidentiality" displayName="正常访问保密级别"/>
	<languageCode code="zh-CN"/>
	<setId/>
	<versionNumber/>
	<recordTarget typeCode="RCT" contextControlCode="OP">
		<patientRole classCode="PAT">
		
			<!--门（急）诊号标识 -->
			<id root="2.16.156.10011.1.11" extension="06445751"/>
			
			<!--处方编号-->
			<id root="2.16.156.10011.1.20" extension="081710391625"/>
			
			<patient classCode="PSN" determinerCode="INSTANCE">
			
				<!--患者身份证号标识-->
				<id root="2.16.156.10011.1.3" extension="440102195501150625"/>
							
				<name>陈秀莲</name>
				<administrativeGenderCode  code="2" displayName="女" codeSystem="2.16.156.10011.2.3.3.4" codeSystemName="生理性别代码表(GB/T 2261.1)"/>
				
				<age unit="岁" value="65"></age>
				
			</patient>
			<!-- 开立科室 -->
			<providerOrganization>
				<id root="2.16.156.10011.1.26"/>
				<name>内科</name>
				<asOrganizationPartOf>
					<wholeOrganization>
						<!-- 机构代码 -->
						<id root="2.16.156.10011.1.5" extension="4554144022"/>
						<name>暨南大学附属第一医院</name>
					</wholeOrganization>
				</asOrganizationPartOf>
			</providerOrganization>
		</patientRole>
	</recordTarget>
	
	<!--创建者-->
	<author typeCode="AUT" contextControlCode="OP">
		<!-- 处方开立日期 -->
		<time value="20200817103901"/>
		<assignedAuthor classCode="ASSIGNED">
			<id root="2.16.156.10011.1.7" extension="1172"/>
			<!-- 处方开立医师 -->
			<assignedPerson>
				<name>林洪</name>
			</assignedPerson>
		</assignedAuthor>
	</author>
	
	<!-- 保管机构 -->
	<custodian typeCode="CST">
	    <assignedCustodian classCode="ASSIGNED">
			<representedCustodianOrganization classCode="ORG" determinerCode="INSTANCE">
				<id root="2.16.156.10011.1.5" extension="4554144022"/>
				<name>暨南大学附属第一医院</name>
		    </representedCustodianOrganization>
		</assignedCustodian>
	</custodian>
	<!-- 处方审核药剂师签名 -->
	<legalAuthenticator>
		<time/>
		<signatureCode/>
		<assignedEntity>
			<id root="2.16.156.10011.1.4" extension="11172"/>
			<code displayName="处方审核药剂师"></code>
			<assignedPerson classCode="PSN" determinerCode="INSTANCE">
				<name>林洪</name>
			</assignedPerson>
		</assignedEntity>
	</legalAuthenticator>
	<!-- 处方调配药剂师签名 -->
	<authenticator>
		<time/>
		<signatureCode/>
		<assignedEntity>
			<id root="2.16.156.10011.1.4" extension="0001745"/>
			<code displayName="处方调配药剂师"></code>
			<assignedPerson classCode="PSN" determinerCode="INSTANCE">
				<name>王昌顺</name>
			</assignedPerson>
		</assignedEntity>
	</authenticator>
	
	<!-- 处方核对药剂师 -->
	<authenticator>
		<time/>
		<signatureCode/>
		<assignedEntity>
			<id root="2.16.156.10011.1.4" extension="11172"/>
			<code displayName="处方核对药剂师"></code>
			<assignedPerson classCode="PSN" determinerCode="INSTANCE">
				<name>林洪</name>
			</assignedPerson>
		</assignedEntity>
	</authenticator>
	<!-- 处方发药药剂师签名 -->
	<authenticator>
		<time/>
		<signatureCode/>
		<assignedEntity>
			<id root="2.16.156.10011.1.4" extension="11172"/>
			<code displayName="处方发药药剂师"></code>
			<assignedPerson classCode="PSN" determinerCode="INSTANCE">
				<name>林洪</name>
			</assignedPerson>
		</assignedEntity>
	</authenticator>
	
	<relatedDocument typeCode="RPLC">
		<parentDocument>
			<id/>
			<setId/>
			<versionNumber/>
		</parentDocument>
	</relatedDocument>
	<component>
		<structuredBody>
			
            <!--诊断记录章节-->
			<component>
				<section>
                   <code code="29548-5" displayName="Diagnosis" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <!--条目：诊断-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE05.01.024.00" displayName="诊断代码" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
                            <value xsi:type="CD"  code="R56.801" displayName="癫痫样发作" codeSystem="2.16.156.10011.2.3.3.11" codeSystemName="ICD-10"/>
                        </observation>
                    </entry>
               </section>
            </component>
			<!--用药章节 1..*-->
            <component>
                <section>
                    <code code="10160-0" codeSystem="2.16.840.1.113883.6.1" displayName="HISTORY OF MEDICATION USE" codeSystemName="LOINC"/>
                    <text/>
                                        <entry>
                        <substanceAdministration classCode="SBADM" moodCode="EVN">
                            <text/>
                            <routeCode  code="1" displayName="口服" codeSystem="2.16.156.10011.2.3.1.158" codeSystemName="用药途径代码表"/>
							<!--用药剂量-单次 -->
							<doseQuantity value="0.50" unit="mg"/>
							<!--用药频率 -->
							<rateQuantity value="01" unit="bid"></rateQuantity>
							<!--药物剂型 -->
							<administrationUnitCode  code="99" displayName="其他剂型(空心胶囊,绷带,纱布,胶布)" codeSystem="2.16.156.10011.2.3.1.211" codeSystemName="药物剂型代码表"/>
							<consumable>
								<manufacturedProduct>
									<manufacturedLabeledDrug>
										<!--药品代码及名称(通用名) -->
										<code/>
										<name>甲钴胺片(弥可保)</name>
									</manufacturedLabeledDrug>
								</manufacturedProduct>
							</consumable>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE08.50.043.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="药物规格"/>
									<value xsi:type="ST">0.5mg*20片(薄膜衣片)</value>
								</observation> 
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE06.00.135.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="药物使用总剂量"/>
									<value xsi:type="PQ" unit="mg" value="10.00"/>
								</observation> 
							</entryRelationship>
                        </substanceAdministration> 
                    </entry>					
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE06.00.294.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方有效天数"/>
							<value xsi:type="PQ" value="7" unit="天" />
						</observation>
					</entry>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE08.50.056.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方药品组号"/>
							<value xsi:type="INT" value="2" />
						</observation>
					</entry>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE06.00.179.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方备注信息"/>
							<value xsi:type="ST">-</value> 
						</observation>
					</entry>                    <entry>
                        <substanceAdministration classCode="SBADM" moodCode="EVN">
                            <text/>
                            <routeCode  code="1" displayName="口服" codeSystem="2.16.156.10011.2.3.1.158" codeSystemName="用药途径代码表"/>
							<!--用药剂量-单次 -->
							<doseQuantity value="150.00" unit="mg"/>
							<!--用药频率 -->
							<rateQuantity value="01" unit="bid"></rateQuantity>
							<!--药物剂型 -->
							<administrationUnitCode  code="99" displayName="其他剂型(空心胶囊,绷带,纱布,胶布)" codeSystem="2.16.156.10011.2.3.1.211" codeSystemName="药物剂型代码表"/>
							<consumable>
								<manufacturedProduct>
									<manufacturedLabeledDrug>
										<!--药品代码及名称(通用名) -->
										<code/>
										<name>(基)奥卡西平片(曲莱)</name>
									</manufacturedLabeledDrug>
								</manufacturedProduct>
							</consumable>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE08.50.043.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="药物规格"/>
									<value xsi:type="ST">150mg*50片</value>
								</observation> 
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE06.00.135.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="药物使用总剂量"/>
									<value xsi:type="PQ" unit="mg" value="7500.00"/>
								</observation> 
							</entryRelationship>
                        </substanceAdministration> 
                    </entry>					
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE06.00.294.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方有效天数"/>
							<value xsi:type="PQ" value="7" unit="天" />
						</observation>
					</entry>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE08.50.056.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方药品组号"/>
							<value xsi:type="INT" value="1" />
						</observation>
					</entry>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE06.00.179.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方备注信息"/>
							<value xsi:type="ST">-</value> 
						</observation>
					</entry>
                </section>
            </component>
			<!--费用章节-->
			<component>
                <section>
                    <code code="48768-6" displayName="PAYMENT SOURCES" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE07.00.004.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方药品金额"/>
							<value xsi:type="MO" value="117.89" currency="元" />
						</observation>
					</entry>
                </section>
            </component>
		</structuredBody>
	</component>
</ClinicalDocument>
'''