class CHDDSRules:

	def  DTRules(self):
		
		rules = []
		rules.append({'conditions' : [{'key' : 'tobacco', 'operator' : '>', 'value' : '22.505'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'tobacco', 'operator' : '=', 'value' : '22.505'}, {'key' : 'sbp', 'operator' : '>', 'value' : '215'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'tobacco', 'operator' : '=', 'value' : '22.505'}, {'key' : 'sbp', 'operator' : '=', 'value' : '215'}, {'key' : 'adiposity', 'operator' : '>', 'value' : '42.115'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'tobacco', 'operator' : '=', 'value' : '22.505'}, {'key' : 'sbp', 'operator' : '=', 'value' : '215'}, {'key' : 'adiposity', 'operator' : '=', 'value' : '42.115'}], 'conclusion' : 'No'})

		return rules
	
	def PartRules(self):
		
		rules = []
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '<=', 'value' : '31'}, {'key' : 'tobacco', 'operator' : '<=', 'value' : '0.5'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'typea', 'operator' : '<=', 'value' : '68'}, {'key' : 'age', 'operator' : '<=', 'value' : '50'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'famhist', 'operator' : '>', 'value' : '0'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'tobacco', 'operator' : '<=', 'value' : '7.6'}, {'key' : 'typea', 'operator' : '>', 'value' : '42'}, {'key' : 'age', 'operator' : '>', 'value' : '47'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'typea', 'operator' : '<=', 'value' : '56'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '7'}, {'key' : 'adiposity', 'operator' : '>', 'value' : '28.95'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'typea', 'operator' : '>', 'value' : '43'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'tobacco', 'operator' : '<=', 'value' : '7.2'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : '1', 'operator' : '=', 'value' : '1'}], 'conclusion' : 'Yes'})

		return rules

	def J48Rules(self):
		
		rules = []
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '<=', 'value' : '31'}, {'key' : 'tobacco', 'operator' : '<=', 'value' : '0.5'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '<=', 'value' : '31'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '0.5'}, {'key' : 'alcohol', 'operator' : '<=', 'value' : '11.1'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '<=', 'value' : '31'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '0.5'}, {'key' : 'alcohol', 'operator' : '>', 'value' : '11.1'}, {'key' : 'famhist', 'operator' : '<=', 'value' : '0'}, {'key' : 'obesity', 'operator' : '<=', 'value' : '25.39'}, {'key' : 'alcohol', 'operator' : '<=', 'value' : '21.19'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '<=', 'value' : '31'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '0.5'}, {'key' : 'alcohol', 'operator' : '>', 'value' : '11.1'}, {'key' : 'famhist', 'operator' : '<=', 'value' : '0'}, {'key' : 'obesity', 'operator' : '<=', 'value' : '25.39'}, {'key' : 'alcohol', 'operator' : '>', 'value' : '21.19'}, {'key' : 'sbp', 'operator' : '<=', 'value' : '118'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '<=', 'value' : '31'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '0.5'}, {'key' : 'alcohol', 'operator' : '>', 'value' : '11.1'}, {'key' : 'famhist', 'operator' : '<=', 'value' : '0'}, {'key' : 'obesity', 'operator' : '<=', 'value' : '25.39'}, {'key' : 'alcohol', 'operator' : '>', 'value' : '21.19'}, {'key' : 'sbp', 'operator' : '>', 'value' : '118'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '<=', 'value' : '31'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '0.5'}, {'key' : 'alcohol', 'operator' : '>', 'value' : '11.1'}, {'key' : 'famhist', 'operator' : '<=', 'value' : '0'}, {'key' : 'obesity', 'operator' : '>', 'value' : '25.39'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '<=', 'value' : '31'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '0.5'}, {'key' : 'alcohol', 'operator' : '>', 'value' : '11.1'}, {'key' : 'famhist', 'operator' : '>', 'value' : '0'}, {'key' : 'tobacco', 'operator' : '<=', 'value' : '2.4'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '<=', 'value' : '31'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '0.5'}, {'key' : 'alcohol', 'operator' : '>', 'value' : '11.1'}, {'key' : 'famhist', 'operator' : '>', 'value' : '0'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '2.4'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '31'}, {'key' : 'typea', 'operator' : '<=', 'value' : '68'}, {'key' : 'age', 'operator' : '<=', 'value' : '50'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '31'}, {'key' : 'typea', 'operator' : '<=', 'value' : '68'}, {'key' : 'age', 'operator' : '>', 'value' : '50'}, {'key' : 'famhist', 'operator' : '<=', 'value' : '0'}, {'key' : 'tobacco', 'operator' : '<=', 'value' : '7.6'}, {'key' : 'tobacco', 'operator' : '<=', 'value' : '4.82'}, {'key' : 'tobacco', 'operator' : '<=', 'value' : '3.96'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '31'}, {'key' : 'typea', 'operator' : '<=', 'value' : '68'}, {'key' : 'age', 'operator' : '>', 'value' : '50'}, {'key' : 'famhist', 'operator' : '<=', 'value' : '0'}, {'key' : 'tobacco', 'operator' : '<=', 'value' : '7.6'}, {'key' : 'tobacco', 'operator' : '<=', 'value' : '4.82'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '3.96'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '31'}, {'key' : 'typea', 'operator' : '<=', 'value' : '68'}, {'key' : 'age', 'operator' : '>', 'value' : '50'}, {'key' : 'famhist', 'operator' : '<=', 'value' : '0'}, {'key' : 'tobacco', 'operator' : '<=', 'value' : '7.6'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '4.82'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '31'}, {'key' : 'typea', 'operator' : '<=', 'value' : '68'}, {'key' : 'age', 'operator' : '>', 'value' : '50'}, {'key' : 'famhist', 'operator' : '<=', 'value' : '0'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '7.6'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '31'}, {'key' : 'typea', 'operator' : '<=', 'value' : '68'}, {'key' : 'age', 'operator' : '>', 'value' : '50'}, {'key' : 'famhist', 'operator' : '>', 'value' : '0'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '31'}, {'key' : 'typea', 'operator' : '>', 'value' : '68'}], 'conclusion' : 'Yes'})
		
		return rules

	def RipperRules(self):

		rules = []
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '=', 'value' : '49.500'}, {'key' : 'tobacco', 'operator' : '=', 'value' : '0.585'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '=', 'value' : '49.500'}, {'key' : 'typea', 'operator' : '=', 'value' : '53.500'}, {'key' : 'ldl', 'operator' : '=', 'value' : '6.270'}, {'key' : 'obesity', 'operator' : '>', 'value' : '25.140'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'famhist', 'operator' : '=', 'value' : '0.500'}, {'key' : 'tobacco', 'operator' : '=', 'value' : '7.605'}, {'key' : 'adiposity', 'operator' : '=', 'value' : '25.470'}, {'key' : 'sbp', 'operator' : '>', 'value' : '123'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '50.500'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '4.140'}, {'key' : 'sbp', 'operator' : '>', 'value' : '159'}, {'key' : 'alcohol', 'operator' : '=', 'value' : '37.545'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'tobacco', 'operator' : '=', 'value' : '8.040'}, {'key' : 'famhist', 'operator' : '=', 'value' : '0.500'}, {'key' : 'typea', 'operator' : '=', 'value' : '49.500'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '50.500'}, {'key' : 'ldl', 'operator' : '>', 'value' : '7.200'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'age', 'operator' : '>', 'value' : '54.500'}, {'key' : 'sbp', 'operator' : '=', 'value' : '151'}, {'key' : 'obesity', 'operator' : '=', 'value' : '27.940'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '6.540'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'ldl', 'operator' : '=', 'value' : '4.320'}, {'key' : 'obesity', 'operator' : '=', 'value' : '25.130'}, {'key' : 'sbp', 'operator' : '=', 'value' : '133'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'typea', 'operator' : '>', 'value' : '66.500'}, {'key' : 'age', 'operator' : '>', 'value' : '43'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'adiposity', 'operator' : '>', 'value' : '28.075'}, {'key' : 'sbp', 'operator' : '>', 'value' : '149'}, {'key' : 'adiposity', 'operator' : '>', 'value' : '31.155'}, {'key' : 'adiposity', 'operator' : '=', 'value' : '38.900'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'typea', 'operator' : '=', 'value' : '54.500'}, {'key' : 'tobacco', 'operator' : '>', 'value' : '4.490'}, {'key' : 'typea', 'operator' : '=', 'value' : '50.500'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'adiposity', 'operator' : '>', 'value' : '28.065'}, {'key' : 'alcohol', 'operator' : '>', 'value' : '13.500'}, {'key' : 'adiposity', 'operator' : '=', 'value' : '30.425'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'tobacco', 'operator' : '=', 'value' : '4.085'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'adiposity', 'operator' : '=', 'value' : '32.765'}, {'key' : 'sbp', 'operator' : '>', 'value' : '135'}, {'key' : 'ldl', 'operator' : '=', 'value' : '6.555'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'ldl', 'operator' : '=', 'value' : '5.600'}, {'key' : 'age', 'operator' : '=', 'value' : '60'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : 'tobacco', 'operator' : '>', 'value' : '5.120'}, {'key' : 'tobacco', 'operator' : '=', 'value' : '6.600'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'ldl', 'operator' : '>', 'value' : '7.845'}], 'conclusion' : 'No'})
		rules.append({'conditions' : [{'key' : 'typea', 'operator' : '>', 'value' : '56'}, {'key' : 'alcohol', 'operator' : '=', 'value' : '27.980'}], 'conclusion' : 'Yes'})
		rules.append({'conditions' : [{'key' : '1', 'operator' : '=', 'value' : '1'}], 'conclusion' : 'No'})

		return rules


# chdObj = CHDDSRules()

# dtRules = chdObj.DTRules()
# print('total DT Rules: ', len(dtRules))

# partRules = chdObj.PartRules()
# print('total PART Rules: ', len(partRules))

# j48Rules = chdObj.J48Rules()
# print('total J48 Rules: ', len(j48Rules))

# ripperRules = chdObj.RipperRules()
# print('total Ripper Rules: ', len(ripperRules))






		