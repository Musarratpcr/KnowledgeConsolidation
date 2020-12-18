from structured.SSMDSRules import SSMDSRules
from structured.PIDDSRules import PIDDSRules
from structured.CHDDSRules import CHDDSRules
from RdrTree import *
import pickle

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

	def calcualteDifference(self, ruleList, duplicateList):
		for index, dupRule in enumerate(duplicateList):
			condition1 = self.GetRuleConditionArray(dupRule['rule1'])
			#condition1.append(rule['conclusion'])

			for i, rule  in enumerate(ruleList):
				condition2 = self.GetRuleConditionArray(rule)
				#condition2.append(ruleList[i]['conclusion'])
				if set(condition1) == set(condition2):
					ruleList.remove(rule)
		return ruleList

	def getConflictedRules(self, rules):

		Conflictes  = []

		for index, rule in enumerate(rules):
			condition1 = self.GetRuleConditionArray(rule)
			
			for i  in range(index + 1, len(rules)):
				condition2 = self.GetRuleConditionArray(rules[i])
				
				if set(condition1) == set(condition2) and rule['conclusion'] != rules[i]['conclusion']:
					Conflictes.append({"rule1" :  rule, "rule2" : rules[i]})

		return Conflictes 

	def toProductionRuleString(self, ruleList):
		productionRuleList = []
		for rule in ruleList:
			productionRule = " IF "
			for condition in rule['conditions']:
				productionRule += condition['key'] + " " + condition['operator'] + " " + condition['value'] + " AND "
			
			productionRule = "".join(productionRule.rsplit(" AND ", 1))
			productionRule += " THEN " + rule['conclusion']

			productionRuleList.append(productionRule)

		productionRuleList = sorted(productionRuleList, key=len)
		
		return "\r\n".join(productionRuleList)

	def getConslidatedRules(self, ruleSet):
		
		recommendations = {}
		knowledegBase = Tree()
		
		#knowledegBase.append({'conditions': [{'key': '1', 'operator': '=', 'value': '1'}], 'conclusion': 'No Disease'})

		for genRule in ruleSet:
			if(genRule['conclusion'] not in recommendations.keys()):
				recommendations[genRule['conclusion']] = [genRule]
			else:
				recommendations[genRule['conclusion']].append(genRule)


		for genRuleConclusion in recommendations:
			
			# print(genRuleConclusion)
			# print(recommendations[genRuleConclusion])

			for genRule in recommendations[genRuleConclusion]:

				# print('genRule', genRule)
				print(".", end =" ")
				knowledegBase.addRuleNode(None,genRule)
			print("")
			print(len(recommendations[genRuleConclusion]), 'Rules for ', genRuleConclusion, ' added')
			
				
				# conclusionGroupsInKB = []
				# ruleFound = false
				# for rdrRuleRef in knowledegBase:
				# 	if rdrRuleRef['conclusion'] == genRuleConclusion:
				# 		conclusionGroupsInKB.append(rdrRuleRef)
				# 		ruleFound = true
				# 		break
				# if not ruleFound : 
				# knowledegBase.addRuleNode(genRule)

						
			# print('conclusionGroupsInKB: ', conclusionGroupsInKB)
			
			# for rdrRuleRef in conclusionGroupsInKB:
			# 	rdrRuleRef.append(genRule)
				
			# knowledegBase.append({genRuleConclusion : })

		# knowledegBase.printTree()

		return knowledegBase
		


rulesObj =  Rules()
ssmRules = rulesObj.getSSMRules()
pidRules = rulesObj.getPIDRules()
chdRules = rulesObj.getCHDRules()

rules = ssmRules + pidRules + chdRules

# print('total Rule: ', len(rules))
# print(rules)

duplicateRules = rulesObj.getDuplicateRules(rules)
# print('total duplicate Rules: ', len(duplicateRules))
# print(duplicateRules)

rulesWithoutDuplicates =  rulesObj.calcualteDifference(rules, duplicateRules)

conflictedRules = rulesObj.getConflictedRules(rules)
# print('total conflicted Rules: ', len(conflictedRules))
# print(conflictedRules)

rulesWithoutConflicts = rulesObj.calcualteDifference(rulesWithoutDuplicates, conflictedRules)
#rulesWithoutConflicts90 = rulesWithoutConflicts[0:150]
print('remaining Rule: ', len(rulesWithoutConflicts))

# print(rulesObj.toProductionRuleString(rulesWithoutConflicts))

consolidatedRules = rulesObj.getConslidatedRules(rulesWithoutConflicts)
# print(' getConslidatedRules : ', len(consolidatedRules))

with open("rdrTree.txt", "w") as rdr_file:
	strRdrTree = consolidatedRules.getTreeAsString()
	rdr_file.write(strRdrTree)

