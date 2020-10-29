# -*- coding: utf-8 -*-
"""
    @Time 2020/10/26 22:20
    @Author wangjiaming
    @Version V0.1
    @File XmlData
    @Desc:
"""
xml='''<?xml version="1.0" encoding="UTF-8"?>
<ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:mif="urn:hl7-org:v3/mif" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 ..\sdschemas\CDA.xsd">

	<realmCode code="CN"/>
	<typeId root="2.16.840.1.113883.1.3" extension="POCD_MT000040"/>
	<templateId  root="2.16.156.10011.2.1.1.21"/>
	
	<!-- 文档流水号 -->
	<id root="2.16.156.10011.1.1" extension="0001201709100002S"/>
	
	<code code="C0001" codeSystem="2.16.156.10011.2.4" codeSystemName="卫生信息共享文档规范编码体系"></code>
	<title>病历概要</title>
	
	<!-- 文档机器生成时间 -->
	<effectiveTime value="20171115093803"/>

	<confidentialityCode code="N" codeSystem="2.16.840.1.113883.5.25" codeSystemName="Confidentiality" displayName="正常访问保密级别"/>
	<languageCode code="zh-CN"/>
	<setId/>
	<versionNumber/>

	<recordTarget typeCode="RCT" contextControlCode="OP">
		<patientRole classCode="PAT">
		 
			<!--健康档案标识号-->
			<id xCheck="1..1" xCheckKey="root" xTable="TB_SD1_PERSON" xKey="JKDABSH" xValue="extension" root="2.16.156.10011.1.2" extension="0001201709100002S"/>
			
			<!--健康卡号-->
			<id xCheck="1..1" xCheckKey="root" xTable="TB_SD1_PERSON" xKey="JKKH" xValue="extension"  root="2.16.156.10011.1.19" extension="-"/>
			
			<addr use="H">
				<houseNumber xCheck="1..1" xTable="TB_SD1_PERSON" xKey="HOUSEHOLD_ADDR_HOUSENUMBER" xValue="text">黄埔大道西421号906房</houseNumber>
				<streetName xCheck="1..1" xTable="TB_SD1_PERSON" xKey="HOUSEHOLD_ADDR_STREETNAME" xValue="text"></streetName>
				<township xCheck="1..1" xTable="TB_SD1_PERSON" xKey="HOUSEHOLD_ADDR_TOWNSHIP" xValue="text"></township>
				<county xCheck="1..1" xTable="TB_SD1_PERSON" xKey="HOUSEHOLD_ADDR_COUNTY" xValue="text">天河区</county>
				<city xCheck="1..1" xTable="TB_SD1_PERSON" xKey="HOUSEHOLD_ADDR_CITY" xValue="text">广州市</city>
				<state xCheck="1..1" xTable="TB_SD1_PERSON" xKey="HOUSEHOLD_ADDR_STATE" xValue="text">广东省</state>
				<postalCode xCheck="0..1" xTable="TB_SD1_PERSON" xKey="HOUSEHOLD_ADDR_POSTALCODE" xValue="text">-</postalCode>
			</addr>
			<!-- 患者电话 -->
			<telecom xCkeck="0..*" value="13802447531"/>
			<patient classCode="PSN" determinerCode="INSTANCE">
		
				<!--患者身份证号标识-->
				<id xCheck="1..1" xTable="TB_SD1_PERSON" xKey="ID_NO" xValue="extension" root="2.16.156.10011.1.3" extension="440102195606131463"/>
				<!-- 患者姓名 -->
				<name xCheck="1..*" xTable="TB_SD1_PERSON" xKey="NAME;source_id" xValue="text;z_source_id">唐伟玲</name>
				<!-- 性别代码 -->
				<administrativeGenderCode  xCheck="1..1" xTable="TB_SD1_PERSON" xKey="GENDER_CODE;GENDER_NAME" xValue="code;displayName" code="2" displayName="女性" codeSystem="2.16.156.10011.2.3.3.4" codeSystemName="生理性别代码表(GB/T 2261.1)"/>
				<birthTime xCheck="1..1" xTable="TB_SD1_PERSON" xKey="BIRTH_TIME" xValue="value" value="19560613"/>
				<!-- 婚姻状况代码 -->
				<maritalStatusCode xCheck="1..1" xTable="TB_SD1_PERSON" xKey="MARITAL_STATUS_CODE;MARITAL_STATUS_NAME" xValue="code;displayName" code="20" displayName="已婚" codeSystem="2.16.156.10011.2.3.3.5" codeSystemName="婚姻状况代码表(GB/T 2261.2)"/>
				<!-- 民族 -->
				<ethnicGroupCode xCheck="1..1" xTable="TB_SD1_PERSON" xKey="ETHNIC_GROUP_CODE;ETHNIC_GROUP_NAME" xValue="code;displayName" code="01" displayName="汉族" codeSystem="2.16.156.10011.2.3.3.3" codeSystemName="民族类别代码表(GB 3304)"/>
				<!-- 工作单位 -->
				<employerOrganization>
					<name xCheck="0..*" xTable="TB_SD1_PERSON" xKey="EMPLOYER_ORGANIZATION_NAME" xValue="text">-</name>
					<telecom xCheck="0..*" xTable="TB_SD1_PERSON" xKey="EMPLOYER_ORGANIZATION_TELECOM" xValue="value" value="-"></telecom>
				</employerOrganization>
				<!--职业状况-->
				<occupation>
					<occupationCode  xCheck="0..1" xTable="TB_SD1_PERSON" xKey="OCCUPATION_CODE;OCCUPATION_NAME" xValue="code;displayName" code="80" codeSystem="2.16.156.10011.2.3.3.13" codeSystemName="从业状况(个人身体)代码表(GB/T 2261.4)" displayName="退(离)休人员"/>
				</occupation>
			</patient>
	
		</patientRole>
	</recordTarget>
	
	<!--创建者-->
	<author typeCode="AUT" contextControlCode="OP">
		<!-- 建档日期 -->
		<time xCheck="1..*" xTable="TB_SD1_PERSON" xKey="AUTHOR_TIME" xValue="value" value="20170922001942"/>
		<assignedAuthor classCode="ASSIGNED">
			<id root="2.16.156.10011.1.7" extension="T2245*1"/>
			<!-- 建档者姓名 -->
			<assignedPerson>
				<name xCheck="0..*" xTable="TB_SD1_PERSON" xKey="AUTHOR_NAME" xValue="text">邹燕玲</name>
			</assignedPerson>
			<!-- 建档机构 -->
			<representedOrganization>
				<id xCheck="0..*" xCheckKey="root" xTable="TB_SD1_PERSON" xKey="AUTHOR_MED_CODE" xValue="extension" root="2.16.156.10011.1.5" extension="4554144022"/>
				<name xCheck="0..*" xTable="TB_SD1_PERSON" xKey="AUTHOR_MED_NAME" xValue="text">暨南大学附属第一医院</name>
			</representedOrganization>
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
	
	<!--其他参与者（联系人）@typeCode: NOT(ugent notification contact)，固定值，表示不同的参与者 -->
	<participant typeCode="NOT" xCheck="1..*" xLoopDots="True" xTable="TB_SD1_PARTICIPANT">
		<!--联系人@classCode：CON，固定值，表示角色是联系人 -->
		<associatedEntity classCode="ECON">
			<!--联系人类别，表示与患者之间的关系-->
			<code/>
                        <!--联系人地址-->
			<addr>		
				<houseNumber xCheck="1..*" xTable="TB_SD1_PARTICIPANT" xKey="ADDR_HOUSENUMBER" xValue="text">黄埔大道西421号906房</houseNumber>
				<streetName xCheck="1..*" xTable="TB_SD1_PARTICIPANT" xKey="ADDR_STREETNAME" xValue="text"></streetName>
				<township xCheck="1..*" xTable="TB_SD1_PARTICIPANT" xKey="ADDR_TOWNSHIP" xValue="text"></township>
				<county xCheck="1..*" xTable="TB_SD1_PARTICIPANT" xKey="ADDR_COUNTY" xValue="text">天河区</county>
				<city xCheck="1..*" xTable="TB_SD1_PARTICIPANT" xKey="ADDR_CITY" xValue="text">广州市</city>
				<state xCheck="1..*" xTable="TB_SD1_PARTICIPANT" xKey="ADDR_STATE" xValue="text">广东省</state>
				<postalCode xCheck="1..*" xTable="TB_SD1_PARTICIPANT" xKey="ADDR_POSTALCODE" xValue="text">无</postalCode>
			</addr>
			<!--电话号码-->
			<telecom xCheck="1..*" xTable="TB_SD1_PARTICIPANT" xKey="TELECOM" xValue="value" use="H" value="13802447531"/>
			<!--联系人-->
			<associatedPerson classCode="PSN" determinerCode="INSTANCE">
				<!--姓名-->
				<name xCheck="1..*" xTable="TB_SD1_PARTICIPANT" xKey="NAME;pid;id_no" xValue="text;z_pid;z_id_no">谢耀强</name>
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
		
			<!-- 实验室检验章节 -->
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
									<code code="DE04.50.001.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"  />
									<value xsi:type="CD"  code="5" codeSystem="2.16.156.10011.2.3.1.85" codeSystemName="ABO血型代码表" displayName="不详"/>
								</observation>
							</component>
							<!-- Rh血型 -->
							<component typeCode="COMP" contextConductionInd="true">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE04.50.010.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" />
									<value xsi:type="CD"  code="4" codeSystem="2.16.156.10011.2.3.1.250" codeSystemName="Rh(D)血型代码表" displayName="未查"/>
								</observation>
							</component>
						</organizer>
					</entry>
				</section>
			</component>
			
			<!-- 既往史章节 -->
			<component>
				<section>
					<code code="11348-0" displayName="HISTORY OF PAST ILLNESS" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
					<text/>
					<!-- 疾病史（含外伤） -->
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.10.026.00" displayName="疾病史（含外伤）" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
							<value xsi:type="ST">-</value>
						</observation>
					</entry>
					<!-- 传染病史 -->
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.10.008.00" displayName="传染病史" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
							<value xsi:type="ST">否认“肝炎”、“结核”等传染病史</value>
						</observation>
					</entry>
					
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.10.061.00" displayName="手术史" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
							<value xsi:type="ST">2016年12月因腰椎间盘突出症（L4/L5）行手术治疗；有“子宫肌瘤子宫全切术后”病史；否认其他手术、外伤及药物过敏史</value>
						</observation>
					</entry>

					<!--婚育史条目-->
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.10.098.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="婚育史"/>
							<value xsi:type="ST">已婚已育，育有1男，爱人及子女均体健。</value>
						</observation>
					</entry>
				</section>
			</component>
			
			<!-- 输血章节 -->
			<component>
				<section>
					<code code="56836-0" displayName="History of blood transfusion" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
					<text/>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.10.100.00" displayName="输血史" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
							<value xsi:type="ST">否认输血史</value>
						</observation>
					</entry>
				</section>
			</component>						
			
			<!-- 过敏史章节 -->
			<component>
				<section>
					<code code="48765-2" displayName="Allergies, adverse reactions, alerts" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
					<text/>

					<!--过敏史条目-->
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.10.022.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="过敏史"/>
							<value xsi:type="ST">否认</value>
						</observation>
					</entry>			
				</section>
			</component>
			
			
			<!--预防接种史章节-->
            <component>
                <section>
                    <code code="11369-6" codeSystem="2.16.840.1.113883.6.1" displayName="HISTORY OF IMMUNIZATIONS" codeSystemName="LOINC"/>
                    <text/>
                    <entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.10.101.00" displayName="预防接种史" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
							<value xsi:type="ST">预防接种史不详。</value>
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
							<value xsi:type="ST">出生原籍，未到外地久居。无疫水、毒物接触史。有吸烟史30余年，7~8支/天。无酗酒等不良生活习惯。居住生活条件可。(月经)有吸烟</value>
						</observation>
					</entry>
				</section>
			</component>

			<!--月经史章节-->
			<component>
				<section>
					<code code="49033-4" displayName="Menstrual History" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
					<text/>
					<!--月经史条目-->
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.10.102.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="月经史"/>
							<value xsi:type="ST">-</value>
						</observation>
					</entry>
				</section>
			</component>
			
            <!--家族史章节-->
            <component>
                <section>
                    <code code="10157-6" displayName="HISTORY OF FAMILY MEMBER DISEASES" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
                    <text/>
                    <entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.10.103.00" displayName="家族史" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
							<value xsi:type="ST">否认有遗传疾病史。</value>
						</observation>
                    </entry>
                </section>
            </component>
            
            <!-- 卫生事件章节 --> 
            <component>
				<section>
					<code displayName="卫生事件"></code>
					<text/>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE08.10.026.00" displayName="医疗机构科室名称" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
							<value xsi:type="ST">神经内科病房</value>
						</observation>
					</entry>
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE02.01.060.00" displayName="患者类型代码" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
							<value xsi:type="CD"   code="3" displayName="住院" codeSystem="2.16.156.10011.2.3.1.271" codeSystemName="患者类型代码表"/>	
						</observation>
					</entry>
					
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE01.00.010.00" displayName="门（急）诊号" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
							<value xsi:type="ST">-</value>
						</observation>
					</entry>
					
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE01.00.014.00" displayName="住院号" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
							<value xsi:type="ST">402544</value>
						</observation>
					</entry>					

					<entry>
						<organizer classCode="BATTERY" moodCode="EVN">
							<statusCode/>
							<component>
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE06.00.092.00" displayName="入院时间" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
									<value xsi:type="TS" value=""/>
								</observation>
							</component>
							<component>
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE06.00.017.00" displayName="出院时间" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
									<value xsi:type="TS" value="20170918113326"/>
								</observation>
							</component>							
						</organizer>
					</entry>
					
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE04.01.018.00" displayName="发病日期时间" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
							<value xsi:type="TS" value="20170910"/>
						</observation>
					</entry>					
					<entry>
						<observation classCode="OBS" moodCode="EVN">
							<code code="DE05.10.053.00" displayName="就诊原因" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"></code>
							<!-- 就诊日期时间 DE06.00.062.00-->
							<effectiveTime value="20170910164644"/>
							<value xsi:type="ST">反复头晕5年，加重2月余头晕5年反复头晕5年，加重2月余</value>
						</observation>
					</entry>

                    <!--条目：诊断-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE05.01.024.00" displayName="西医诊断编码" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"><qualifier><name displayName="西医诊断编码"></name></qualifier></code>
                            <value xsi:type="CD"   code="D18.000" codeSystem="2.16.156.10011.2.3.3.11" codeSystemName="ICD-10" displayName="血管瘤"/>
                            <entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE05.10.113.00" displayName="病情转归代码" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
									<value xsi:type="CD"  code="1" codeSystem="2.16.156.10011.2.3.1.148" codeSystemName="病情转归代码表" displayName="治愈"/>
								</observation>
							</entryRelationship>
                        </observation>
                    </entry>
                    
                    <!--条目：诊断-->
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE05.01.024.00" displayName="其他西医诊断编码" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"><qualifier><name displayName="其他西医诊断编码"></name></qualifier></code>
                            <value xsi:type="CD"  code="M91200/0" displayName="血管瘤" codeSystem="2.16.156.10011.2.3.3.11" codeSystemName="ICD-10"/>
                        </observation>
                    </entry>
                   
                 
                    <entry>
                        <procedure classCode="PROC" moodCode="EVN">
							<!-- 手术及操作编码 DE06.00.093.00 -->
                            <code  code="" displayName="" codeSystem="2.16.156.10011.2.3.3.12" codeSystemName="ICD-9-CM"/>
						</procedure>
                    </entry>
                    
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE08.50.022.00" displayName="关键药物名称" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
                            <value xsi:type="ST">-</value>
                            <entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE06.00.136.00" displayName="关键药物用法" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
									<value xsi:type="ST">-</value>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE06.00.129.00" displayName="药物不良反应情况" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
									<value xsi:type="ST">-</value>
								</observation>
							</entryRelationship>
							<entryRelationship typeCode="COMP">
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE06.00.164.00" displayName="中药使用类别代码" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
									<value xsi:type="CD"  code="1" displayName="未使用" codeSystem="2.16.156.10011.2.3.1.157" codeSystemName="中药使用类别代码表"/>
								</observation>
							</entryRelationship>
                        </observation>
                    </entry>

					<entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE06.00.251.00" displayName="其他医学处置" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
							<value xsi:type="ST">-</value>
                        </observation>
                    </entry>
                    	
                    <entry>
                        <observation classCode="OBS" moodCode="EVN">
                            <code code="DE02.01.039.00" displayName="责任医师姓名" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录"/>
							<value xsi:type="ST">张玉生</value>
                        </observation>
                    </entry>
					
					<!-- 费用条目 -->
					<entry>
						<organizer classCode="CLUSTER" moodCode="EVN">
							<statusCode/>
							<component>
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE02.01.044.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="医疗保险类别代码"/>
									<value xsi:type="CD"  code="07" displayName="商业医疗保险" codeSystem="2.16.156.10011.2.3.1.248" codeSystemName="医疗保险类别代码表"/>
								</observation>
							</component>
							
							<component>
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE07.00.007.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="医疗付费方式代码" ></code>
									<value xsi:type="CD"  code="07" codeSystem="2.16.156.10011.2.3.1.269" displayName="全自费" codeSystemName="医疗付费方式代码表"/>
								</observation>
							</component>
							
							<component>
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE07.00.004.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="门诊费用金额"/>
									<value xsi:type="MO" value="0.00" currency="元"/> 
								</observation>
							</component>							
							<component>
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE07.00.010.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="住院费用金额"/>
									<value xsi:type="MO" value="12793.03" currency="元"/>
								</observation>
							</component>
							<component>
								<observation classCode="OBS" moodCode="EVN">
									<code code="DE07.00.001.00" codeSystem="2.16.156.10011.2.2.1" codeSystemName="卫生信息数据元目录" displayName="个人承担费用金额"/>
									<value xsi:type="MO" value="1409.19" currency="元"/> 
								</observation>
							</component>
						</organizer>
					</entry>		
                </section>
            </component>
		</structuredBody>
	</component>
</ClinicalDocument>
'''