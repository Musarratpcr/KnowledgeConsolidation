from structured.SSMDSRules import SSMDSRules
from structured.PIDDSRules import PIDDSRules
from structured.CHDDSRules import CHDDSRules

class Rules:
	def __init__(self):
		self.ssmObj = SSMDSRules()
		self.pidObj = PIDDSRules()
		self.chdObj = CHDDSRules()

	def getSSMRules(self):
		
		rules = []
		dtRules = self.ssmObj.DTRules()
		partRules = self.ssmObj.PartRules()
		j48Rules = self.ssmObj.J48Rules()
		ripperRules = self.ssmObj.RipperRules()

		rules = dtRules + partRules + j48Rules + ripperRules
		
		return rules

	def getPIDRules(self):
		
		rules = []
		dtRules = self.pidObj.DTRules()
		partRules = self.pidObj.PartRules()
		j48Rules = self.pidObj.J48Rules()
		ripperRules = self.pidObj.RipperRules()

		rules = dtRules + partRules + j48Rules + ripperRules
		
		return rules

	def getCHDRules(self):
		
		rules = []
		dtRules = self.chdObj.DTRules()
		partRules = self.chdObj.PartRules()
		j48Rules = self.chdObj.J48Rules()
		ripperRules = self.chdObj.RipperRules()

		rules = dtRules + partRules + j48Rules + ripperRules
		
		return rules

	def GetRuleConditionArray(self, rule):

		conditions = []

		for condition in rule['conditions']:
			conditions.append(condition['key']+":"+condition['operator']+":"+condition['value'])

		return conditions
		
	def getDuplicateRules(self, rules):

		duplicates  = []

		for index, rule in enumerate(rules):
			condition1 = self.GetRuleConditionArray(rule)
			condition1.append(rule['conclusion'])

			for i  in range(index + 1, len(rules)):
				condition2 = self.GetRuleConditionArray(rules[i])
				condition2.append(rules[i]['conclusion'])

				if set(condition1) == set(condition2):
					duplicates.append({"rule1" :  rule, "rule2" : rules[i]})

		return duplicates

	def getConflictedRules(self, rules):

		Conflictes  = []

		for index, rule in enumerate(rules):
			condition1 = self.GetRuleConditionArray(rule)
			
			for i  in range(index + 1, len(rules)):
				condition2 = self.GetRuleConditionArray(rules[i])
				
				if set(condition1) == set(condition2) and rule['conclusion'] != rules[i]['conclusion']:
					Conflictes.append({"rule1" :  rule, "rule2" : rules[i]})

		return Conflictes 


rulesObj =  Rules()
ssmRules = rulesObj.getSSMRules()
pidRules = rulesObj.getPIDRules()
chdRules = rulesObj.getCHDRules()

rules = ssmRules + pidRules + chdRules

duplicateRules = rulesObj.getDuplicateRules(rules)
print('total duplicate Rules: ', len(duplicateRules))
print(duplicateRules)

conflictedRules = rulesObj.getConflictedRules(rules)
print('total conflicted Rules: ', len(conflictedRules))
print(conflictedRules)
