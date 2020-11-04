# -*- coding: utf-8 -*-
"""
    @Time 2020/10/29 14:24
    @Author wangjiaming
    @Version V0.1
    @File XmlP4Data
    @Desc:
"""
xml='''<?xml version="1.0" encoding="UTF-8"?>
<ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:mif="urn:hl7-org:v3/mif" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 ..\sdschemas\SDA.xsd">

	<realmCode code="CN"/>
	<typeId root="2.16.840.1.113883.1.3" extension="POCD_MT000040"/>
	<templateId  root="2.16.156.10011.2.1.1.24"/>
	<!-- 文档流水号 -->
	<id root="2.16.156.10011.1.1" extension="RN001"/>
	<code code="C0004" codeSystem="2.16.156.10011.2.4" codeSystemName="卫生信息共享文档编码体系"></code>
	<title>西药处方</title>
	<!-- 文档机器生成时间 -->
	<effectiveTime value="20121024154823"/>
	<confidentialityCode code="N" codeSystem="2.16.840.1.113883.5.25" codeSystemName="Confidentiality" displayName="正常访问保密级别"/>
	<languageCode code="zh-CN"/>
	<setId/>
	<versionNumber/>

	<recordTarget typeCode="RCT" contextControlCode="OP">
		<patientRole classCode="PAT">
		
			<!--门（急）诊号标识 -->
			<id xCheck="1..1" xUniqueKey="root" xTable="TB_SD4_PERSON" xKey="SOURCE_ID;MZJZBS" xValue="Z_SOURCE_ID;extension" root="2.16.156.10011.1.11" extension="E10000000"/>
			
			<!--处方编号-->
			<id  xCheck="1..1" xUniqueKey="root" xTable="TB_SD4_PERSON" xKey="CFBM" xValue="extension"  root="2.16.156.10011.1.20" extension="E10000000"/>
			
			<patient classCode="PSN" determinerCode="INSTANCE">
			
				<!--患者身份证号标识-->
				<id xCheck="1..*" xUniqueKey="root" xTable="TB_SD4_PERSON" xKey="ID_NO" xValue="extension"  root="2.16.156.10011.1.3" extension="420106201101011919"/>
				<name xCheck="1..*" xTable="TB_SD4_PERSON" xKey="NAME" xValue="text" >贾小明</name>
				<administrativeGenderCode xCheck="1..1" xTable="TB_SD4_PERSON" xKey="XBDM" xValue="code"  code="1" codeSystem="2.16.156.10011.2.3.3.4" codeSystemName="生理性别代码表（GB/T 2261.1）"/>
				<age xCheck="0..1" xTable="TB_SD4_PERSON" xKey="nldw;nl" xValue="unit;value" unit="岁" value="45"></age>
				
			</patient>
			<!-- 开立科室 -->
			<providerOrganization>
				<id xCheck="0..1" xUniqueKey="root" xTable="TB_SD4_BODY" xKey="ksbm" xValue="extension" root="2.16.156.10011.1.26" extension="科室编码"/>
				<name xCheck="0..1" xTable="TB_SD4_BODY" xKey="ksmc" xValue="text">皮肤科</name>
				<asOrganizationPartOf>
					<wholeOrganization>
						<!-- 机构代码 -->
						<id xCheck="0..1" xTable="TB_SD4_BODY" xKey="MED_CODE" xValue="extension" xUniqueKey="root"  root="2.16.156.10011.1.5" extension="12353"/>
						<name xCheck="0..1" xTable="TB_SD4_BODY" xKey="MED_NAME" xValue="text">机构名称</name>
					</wholeOrganization>
				</asOrganizationPartOf>
			</providerOrganization>
		</patientRole>
	</recordTarget>
	
	<!--创建者-->
	<author typeCode="AUT" contextControlCode="OP">
		<!-- 处方开立日期 -->
		<time xCheck="1..*" xTable="TB_SD4_BODY" xKey="P_ID;KFSJ" xValue="Z_PID;value" value="20120909"/>
		<assignedAuthor classCode="ASSIGNED">
			<id xCheck="1..*" xUniqueKey="root" xTable="TB_SD4_BODY" xKey="YSGH" xValue="extension" root="2.16.156.10011.1.7" extension="234234234"/>
			<!-- 处方开立医师 -->
			<assignedPerson>
				<name xCheck="0..*" xTable="TB_SD4_BODY" xKey="YSXM" xValue="text">李医生</name>
			</assignedPerson>
		</assignedAuthor>
	</author>
	
	<!-- 保管机构 -->
	<custodian typeCode="CST">
	    <assignedCustodian classCode="ASSIGNED">
			<representedCustodianOrganization classCode="ORG" determinerCode="INSTANCE">
				<id xCheck="1..*" xUniqueKey="root" xTable="TB_SD4_BODY" xKey="BGJG" xValue="extension" root="2.16.156.10011.1.5" extension="医疗卫生机构编号"/>
				<name xCheck="0..*" xTable="TB_SD4_BODY" xKey="BGMC" xValue="text">xx医院</name>
		    </representedCustodianOrganization>
		</assignedCustodian>
	</custodian>

	<!-- 处方审核药剂师签名 -->
	<legalAuthenticator>
		<time xCheck="1..*" xTable="TB_SD4_BODY" xKey="SHSJ" xValue="value" />
		<signatureCode/>
		<assignedEntity>
			<id xCheck="1..*"  xTable="TB_SD4_BODY" xKey="SHYSGH" xValue="extension"  root="2.16.156.10011.1.4" extension="医务人员编号"/>
			<code displayName="处方审核药剂师"></code>
			<assignedPerson classCode="PSN" determinerCode="INSTANCE">
				<name xCheck="1..*" xTable="TB_SD4_BODY" xKey="SHYSMC" xValue="text">刘医生</name>
			</assignedPerson>
		</assignedEntity>
	</legalAuthenticator>

	<!-- 处方调配药剂师签名 -->
	<authenticator>
		<time xCheck="1..*" xUniqueKey="d:..../code/displayName" xTable="TB_SD4_BODY" xKey="TPSJ" xValue="value" />
		<signatureCode/>
		<assignedEntity>
			<id xCheck="1..*" xUniqueKey="d:./code/displayName" xTable="TB_SD4_BODY" xKey="TPYSGH" xValue="extension" root="2.16.156.10011.1.4" extension="医务人员编号"/>
			<code displayName="处方调配药剂师"></code>
			<assignedPerson classCode="PSN" determinerCode="INSTANCE">
				<name xCheck="1..*" xUniqueKey="u:../code/displayName" xTable="TB_SD4_BODY" xKey="TPYSMC" xValue="text">钱医生</name>
			</assignedPerson>
		</assignedEntity>
	</authenticator>
	
	<!-- 处方核对药剂师 -->
	<authenticator>
		<time xCheck="1..*" xUniqueKey="d:..../code/displayName" xTable="TB_SD4_BODY" xKey="HDSJ" xValue="value" />
		<signatureCode/>
		<assignedEntity>
			<id xCheck="1..*" xUniqueKey="d:./code/displayName" xTable="TB_SD4_BODY" xKey="HDYSGH" xValue="extension" root="2.16.156.10011.1.4" extension="医务人员编号"/>
			<code displayName="处方核对药剂师"></code>
			<assignedPerson classCode="PSN" determinerCode="INSTANCE">
				<name xCheck="1..*" xUniqueKey="u:../code/displayName" xTable="TB_SD4_BODY" xKey="HDYSMC" xValue="text">孙医生</name>
			</assignedPerson>
		</assignedEntity>
	</authenticator>

	<!-- 处方发药药剂师签名 -->
	<authenticator>
		<time xCheck="1..*" xUniqueKey="d:..../code/displayName" xTable="TB_SD4_BODY" xKey="FYSJ" xValue="value" />
		<signatureCode/>
		<assignedEntity>
			<id xCheck="1..*" xUniqueKey="d:./code/displayName" xTable="TB_SD4_BODY" xKey="FYYSGH" xValue="extension" root="2.16.156.10011.1.4" extension="医务人员编号"/>
			<code displayName="处方发药药剂师"></code>
			<assignedPerson classCode="PSN" determinerCode="INSTANCE">
				<name xCheck="1..*" xUniqueKey="u:../code/displayName" xTable="TB_SD4_BODY" xKey="FYYSMC" xValue="text">任医生</name>
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
	<componentOf>
		<encompassingEncounter classCode="ENC" moodCode="EVN">
			<effectiveTime/>
			<id root="2.16.156.10011.1.99.99.2.010" extension="1234455"/>
			<id root="2.16.156.10011.1.99.99.2.001" extension="123343443"/>
		</encompassingEncounter>
	</componentOf>

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
                            <value xCheck="1..1" xUniqueKey="u:./code/code" xTable="TB_SD4_BODY" xKey="ZDDM" xValue="code" xsi:type="CD" code="1" codeSystem="2.16.156.10011.2.3.3.11.3" codeSystemName="诊断代码表（ICD-10）"></value>
                        </observation>
                    </entry>
               </section>
            </component>

			<!--用药章节 1..*-->
            <component>
                <section>
                    <code code="10160-0" codeSystem="2.16.840.1.113883.6.1" displayName="HISTORY OF MEDICATION USE" codeSystemName="LOINC"/>
                    <text/>
                    <entry xCheck="1..*" xLoopDots="True" xTable="TB_SD4_DRUG_DETAILE">
                        <substanceAdministration classCode="SBADM" moodCode="EVN">
                            <text/>
                            <routeCode xCheck="1..*" xUniqueKey="codeSystem" xTable="TB_SD4_DRUG_DETAILE" xKey="P_ID;INFO_ID;YYTJBM" xValue="z_pid;z_info_id;code" code="1" codeSystem="2.16.156.10011.2.3.1.158" codeSystemName="用药途径代码表"/>
							<!--用药剂量-单次 -->
							<doseQuantity xCheck="1..*" xTable="TB_SD4_DRUG_DETAILE" xKey="YYJLDW;YYJL" xValue="unit;value" value="20" unit="mg"/>
							<!--用药频率 -->
							<rateQuantity xCheck="1..*" xTable="TB_SD4_DRUG_DETAILE" xKey="YYPLDW;YYPL" xValue="unit;value" value="3" unit="次/日"></rateQuantity>
							<!--药物剂型 -->
							<administrationUnitCode xCheck="1..*" xUniqueKey="codeSystem" xTable="TB_SD4_DRUG_DETAILE" xKey="YWJX" xValue="code" code="1" codeSystem="2.16.156.10011.2.3.1.211" displayName="药物剂型代码表"></administrationUnitCode>
							<consumable>
								<manufacturedProduct>
									<manufacturedLabeledDrug>
										<!--药品代码及名称(通用名) -->
										<code/>
										<name xCheck="1..*" xTable="TB_SD4_DRUG_DETAILE" xKey="YWMC" xValue="text">氢氯噻臻</name>
									</manufacturedLabeledDrug>
								</manufacturedProduct>
							</consumable>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE08.50.043.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="药物规格"/>
									<value xCheck="1..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="YWGG" xValue="text" xsi:type="ST">规格描述</value>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE06.00.135.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="药物使用总剂量"/>
									<value xCheck="1..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="YWSYZJL" xValue="value" xsi:type="PQ" value="3"></value>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1048" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="药物使用总剂量单位"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="YWSYZJLDW" xValue="value" xsi:type="ST" value="mg"/>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1043" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="处方项目明细号码"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="CFXMMXHM" xValue="text" xsi:type="ST" value="1243546546"/>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1044" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="（药品的）生产批号"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="SCPH" xValue="value" xsi:type="ST" value="34546565"/>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1045" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="（药品的）有效期至"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="YXQ" xValue="value" xsi:type="ST" value="20200304"/>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1046" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="药物编码（医保）"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="YBBM" xValue="value" xsi:type="ST" value="67999"/>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1047" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="药物编码（院内）"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="YNBM" xValue="value" xsi:type="ST" value="886655"/>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1049" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="药物包装单位"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="BZDW" xValue="value" xsi:type="ST" value="盒"/>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1050" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="药物单价"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="YWDW" xValue="value" xsi:type="PQ" unit="元" value="3"/>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1051" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="药物包装数量"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="BZSL" xValue="value" xsi:type="PQ" value="3"/>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="1052" codeSystem="2.16.156.10011.1.99.99.1.008" codeSystemName="南京卫生信息数据元目录" displayName="药物金额"/>
									<value xCheck="0..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_DETAILE" xKey="YWJE;YWJEDW" xValue="value;unit" xsi:type="PQ" unit="元" value="3"/>
								</observation>
							</entryRelationship>

                        </substanceAdministration>
                    </entry>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE06.00.294.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方有效天数"/>
							<value xCheck="1..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_INFO" xKey="P_ID;CFYXTS;CFYXTSDW" xValue="Z_ID;value;unit"  xsi:type="PQ" value="3" unit="天"></value> 
						</observation>
					</entry>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE08.50.056.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方药品组号"/>
							<value xCheck="1..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_INFO" xKey="CFYPZH" xValue="value" xsi:type="INT" value="4"></value> 
						</observation>
					</entry>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE06.00.179.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="处方备注信息"/>
							<value xCheck="1..*" xUniqueKey="u:./code/code" xTable="TB_SD4_DRUG_INFO" xKey="CFBZXX" xValue="text" xsi:type="ST">备注信息描述</value> 
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
							<value xCheck="1..1" xUniqueKey="u:./code/code" xTable="TB_SD4_BODY" xKey="CFYPJE;CFYPJEDW" xValue="value;currency"  xsi:type="MO" value="4" currency="元"></value> 
						</observation>
					</entry>
                </section>
            </component>
		</structuredBody>
	</component>
</ClinicalDocument>
'''