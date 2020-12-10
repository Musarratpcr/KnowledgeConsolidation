class SSMDSRules:

	def  DTRules(self):
		
		rules = []
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '102'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '102'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '>', 'value' : '5.700'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '6.450'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '>', 'value' : '5.700'}, {'key' : 'HbA1c', 'operator' : '=', 'value' : '6.450'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '>', 'value' : '5.700'}, {'key' : 'HbA1c', 'operator' : '=', 'value' : '6.450'}, {'key' : 'FPG', 'operator' : '>', 'value' : '118.500'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '>', 'value' : '5.700'}, {'key' : 'HbA1c', 'operator' : '=', 'value' : '6.450'}, {'key' : 'FPG', 'operator' : '=', 'value' : '118.500'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '=', 'value' : '5.700'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '=', 'value' : '5.700'}, {'key' : 'FPG', 'operator' : '>', 'value' : '105.500'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '=', 'value' : '5.700'}, {'key' : 'FPG', 'operator' : '=', 'value' : '105.500'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '>', 'value' : '199'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '=', 'value' : '199'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '=', 'value' : '199'}, {'key' : 'FPG', 'operator' : '>', 'value' : '125'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '=', 'value' : '199'}, {'key' : 'FPG', 'operator' : '=', 'value' : '125'}, {'key' : 'PPG', 'operator' : '>', 'value' : '140'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '=', 'value' : '199'}, {'key' : 'FPG', 'operator' : '=', 'value' : '125'}, {'key' : 'PPG', 'operator' : '=', 'value' : '140'}, {'key' : 'FPG', 'operator' : '>', 'value' : '105'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '=', 'value' : '199'}, {'key' : 'FPG', 'operator' : '=', 'value' : '125'}, {'key' : 'PPG', 'operator' : '=', 'value' : '140'}, {'key' : 'FPG', 'operator' : '=', 'value' : '105'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'previousPPG', 'operator' : '>', 'value' : '171'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'previousPPG', 'operator' : '=', 'value' : '171'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '>', 'value' : '123.500'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '=', 'value' : '123.500'}, {'key' : 'previousFPG', 'operator' : '>', 'value' : '100.500'}], 'conclusion' : 'previousPPG'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '=', 'value' : '123.500'}, {'key' : 'previousFPG', 'operator' : '>', 'value' : '100.500'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '6.550'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '=', 'value' : '123.500'}, {'key' : 'previousFPG', 'operator' : '>', 'value' : '100.500'}, {'key' : 'HbA1c', 'operator' : '=', 'value' : '6.550'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '=', 'value' : '123.500'}, {'key' : 'previousFPG', 'operator' : '=', 'value' : '100.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '103.500'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '=', 'value' : '123.500'}, {'key' : 'previousFPG', 'operator' : '=', 'value' : '100.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '103.500'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '=', 'value' : '123.500'}, {'key' : 'previousFPG', 'operator' : '=', 'value' : '100.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '103.500'}, {'key' : 'previousPPG', 'operator' : '>', 'value' : '159.500'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '=', 'value' : '123.500'}, {'key' : 'previousFPG', 'operator' : '=', 'value' : '100.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '103.500'}, {'key' : 'previousPPG', 'operator' : '=', 'value' : '159.500'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199.500'}, {'key' : 'RPG', 'operator' : '>', 'value' : '327'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199.500'}, {'key' : 'RPG', 'operator' : '=', 'value' : '327'}, {'key' : 'RPG', 'operator' : '>', 'value' : '316'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199.500'}, {'key' : 'RPG', 'operator' : '=', 'value' : '327'}, {'key' : 'RPG', 'operator' : '=', 'value' : '316'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199.500'}, {'key' : 'RPG', 'operator' : '=', 'value' : '327'}, {'key' : 'RPG', 'operator' : '=', 'value' : '316'}, {'key' : 'Sx', 'operator' : '>', 'value' : '0.500'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199.500'}, {'key' : 'RPG', 'operator' : '=', 'value' : '327'}, {'key' : 'RPG', 'operator' : '=', 'value' : '316'}, {'key' : 'Sx', 'operator' : '=', 'value' : '0.500'}, {'key' : 'RPG', 'operator' : '>', 'value' : '232.500'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199.500'}, {'key' : 'RPG', 'operator' : '=', 'value' : '327'}, {'key' : 'RPG', 'operator' : '=', 'value' : '316'}, {'key' : 'Sx', 'operator' : '=', 'value' : '0.500'}, {'key' : 'RPG', 'operator' : '=', 'value' : '232.500'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '=', 'value' : '199.500'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '=', 'value' : '199.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '103.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '125.500'}, {'key' : 'RPG', 'operator' : '>', 'value' : '181'}, {'key' : 'RPG', 'operator' : '>', 'value' : '194'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '=', 'value' : '199.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '103.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '125.500'}, {'key' : 'RPG', 'operator' : '>', 'value' : '181'}, {'key' : 'RPG', 'operator' : '=', 'value' : '194'}, {'key' : 'FPG', 'operator' : '>', 'value' : '134'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '=', 'value' : '199.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '103.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '125.500'}, {'key' : 'RPG', 'operator' : '>', 'value' : '181'}, {'key' : 'RPG', 'operator' : '=', 'value' : '194'}, {'key' : 'FPG', 'operator' : '=', 'value' : '134'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '=', 'value' : '199.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '103.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '125.500'}, {'key' : 'RPG', 'operator' : '=', 'value' : '181'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '=', 'value' : '199.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '103.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '125.500'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '=', 'value' : '199.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '103.500'}], 'conclusion' : 'No DM'})
		
		return rules
	
	def PartRules(self):
		
		rules = []
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199'}, {'key' : 'previousPPG ', 'operator' : '>', 'value' : '190'}, {'key' : 'PPG ', 'operator' : '>', 'value' : '174'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '<=', 'value' : '5.7'}, {'key' : 'FPG', 'operator' : '<=', 'value' : '101'}, {'key' : 'PPG ', 'operator' : '>', 'value' : '142'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199'}, {'key' : 'Sx', 'operator' : '>', 'value' : '0'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '<=', 'value' : '122'}, {'key' : 'HbA1c', 'operator' : '<=', 'value' : '6.4'}, {'key' : 'PPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'FPG', 'operator' : '<=', 'value' : '101'}, {'key' : 'FPG', 'operator' : '<=', 'value' : '126'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '>', 'value' : '121'}, {'key' : 'OGTT', 'operator' : '<=', 'value' : '0'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '>', 'value' : '6.4'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'FPG', 'operator' : '<=', 'value' : '105'}, {'key' : 'previousPPG', 'operator' : '<=', 'value' : '140'}, {'key' : 'OGTT', 'operator' : '<=', 'value' : '0'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'FPG', 'operator' : '<=', 'value' : '126'}, {'key' : 'previousPPG', 'operator' : '<=', 'value' : '140'}, {'key' : 'PPG', 'operator' : '>', 'value' : '140'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '>', 'value' : '199'}, {'key' : 'OGTT', 'operator' : '>', 'value' : '0'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '<=', 'value' : '100'}, {'key' : 'PPG', 'operator' : '>', 'value' : '140'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '100'}, {'key' : 'FPG', 'operator' : '<=', 'value' : '126'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '11'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : '1', 'operator' : '=', 'value' : '1'}], 'conclusion' : 'No DM'})

		return rules

	def J48Rules(self):
		
		rules = []
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'HbA1c', 'operator' : '<=', 'value' : '5.8'}, {'key' : 'FPG', 'operator' : '<=', 'value' : '101'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'HbA1c', 'operator' : '<=', 'value' : '5.8'}, {'key' : 'FPG', 'operator' : '>', 'value' : '101'}, {'key' : 'FPG', 'operator' : '<=', 'value' : '126'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'HbA1c', 'operator' : '<=', 'value' : '5.8'}, {'key' : 'FPG', 'operator' : '>', 'value' : '101'}, {'key' : 'FPG', 'operator' : '>', 'value' : '126'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '5.8'}, {'key' : 'HbA1c', 'operator' : '<=', 'value' : '6.4'}, {'key' : 'PPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'FPG', 'operator' : '<=', 'value' : '126'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '5.8'}, {'key' : 'HbA1c', 'operator' : '<=', 'value' : '6.4'}, {'key' : 'PPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'FPG', 'operator' : '>', 'value' : '126'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '5.8'}, {'key' : 'HbA1c', 'operator' : '<=', 'value' : '6.4'}, {'key' : 'PPG', 'operator' : '>', 'value' : '199'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '<=', 'value' : '199'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '5.8'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '6.4'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199'}, {'key' : 'previousPPG', 'operator' : '<=', 'value' : '190'}, {'key' : 'Sx', 'operator' : '<=', 'value' : '0'}, {'key' : 'HbA1c', 'operator' : '<=', 'value' : '6.4'}, {'key' : 'previousPPG', 'operator' : '<=', 'value' : '139'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199'}, {'key' : 'previousPPG', 'operator' : '<=', 'value' : '190'}, {'key' : 'Sx', 'operator' : '<=', 'value' : '0'}, {'key' : 'HbA1c', 'operator' : '<=', 'value' : '6.4'}, {'key' : 'previousPPG', 'operator' : '>', 'value' : '139'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199'}, {'key' : 'previousPPG', 'operator' : '<=', 'value' : '190'}, {'key' : 'Sx', 'operator' : '<=', 'value' : '0'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '6.4'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199'}, {'key' : 'previousPPG', 'operator' : '<=', 'value' : '190'}, {'key' : 'Sx', 'operator' : '>', 'value' : '0'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '>', 'value' : '199'}, {'key' : 'previousPPG', 'operator' : '>', 'value' : '190'}], 'conclusion' : 'DM'})
	

		return rules

	def RipperRules(self):

		rules = []
		rules.append({'conditions' : [{'key' : 'RPG', 'operator' : '=', 'value' : '327'}, {'key' : 'RPG', 'operator' : '>', 'value' : '199.500'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '=', 'value' : '5.750'}, {'key' : 'HbA1c', 'operator' : '=', 'value' : '5.150'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'PPG', 'operator' : '=', 'value' : '199.500'}, {'key' : 'OGTT', 'operator' : '>', 'value' : '0.500'}, {'key' : 'PPG', 'operator' : '>', 'value' : '139.500'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '99.500'}, {'key' : 'PPG', 'operator' : '=', 'value' : '169'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '126.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '142.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '140.500'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '151.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '159'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '>', 'value' : '5.950'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '6.950'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '7.650'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '110.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '125.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '133.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '145'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '126.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '148.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '130.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '131.500'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '126.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '129.500'}, {'key' : 'RPG', 'operator' : '>', 'value' : '194'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '126.500'}, {'key' : 'RPG', 'operator' : '=', 'value' : '181'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '=', 'value' : '5.750'}, {'key' : 'previousHbA1c', 'operator' : '=', 'value' : '5.700'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '110.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '125.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '148.500'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '110.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '109'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'previousFPG', 'operator' : '=', 'value' : '123.500'}, {'key' : 'previousFPG', 'operator' : '>', 'value' : '112'}], 'conclusion' : 'Prediabetes'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '107.500'}, {'key' : 'HbA1c', 'operator' : '=', 'value' : '6.450'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '5.700'}, {'key' : 'FPG', 'operator' : '>', 'value' : '99.500'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '99.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '88.500'}, {'key' : 'Sx', 'operator' : '>', 'value' : '0.500'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '99.500'}, {'key' : 'PPG', 'operator' : '>', 'value' : '187.500'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '98.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '88.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '89.500'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '94.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '79.500'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '98.500'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '6.900'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '102'}, {'key' : 'FPG', 'operator' : '>', 'value' : '98.500'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '126.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '131.500'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '94.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '124.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '129.500'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'HbA1c', 'operator' : '>', 'value' : '5.9500'}, {'key' : 'HbA1c', 'operator' : '=', 'value' : '6.350'}, {'key' : 'HbA1c', 'operator' : '=', 'value' : '6.150'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '94.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '124.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '128.500'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '6.450'}], 'conclusion' : 'DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '>', 'value' : '125'}], 'conclusion' : 'Recheck'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '94.500'}, {'key' : 'HbA1c', 'operator' : '>', 'value' : '5.550'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : 'FPG', 'operator' : '=', 'value' : '94.500'}, {'key' : 'FPG', 'operator' : '>', 'value' : '83.500'}, {'key' : 'FPG', 'operator' : '=', 'value' : '91'}], 'conclusion' : 'No DM'})
		rules.append({'conditions' : [{'key' : '1', 'operator' : '=', 'value' : '1'}], 'conclusion' : 'Prediabetes'})
		
		return rules


# ssmObj = SSMDSRules()

# dtRules = ssmObj.DTRules()
# print('total DT Rules: ', len(dtRules))

# partRules = ssmObj.PartRules()
# print('total PART Rules: ', len(partRules))

# j48Rules = ssmObj.J48Rules()
# print('total J48 Rules: ', len(j48Rules))

# ripperRules = ssmObj.RipperRules()
# print('total Ripper Rules: ', len(ripperRules))






		