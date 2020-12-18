#!/usr/bin/env python

class Node(object):
    def __init__(self, conclusion, conditions, conditionsMatched):
        self.conclusion = conclusion
        self.conditions = conditions
        self.children = []
        self.conditionsMatched = conditionsMatched

    def printNode(self, separatorStr):
        productionRule = separatorStr + " IF "
        for condition in self.conditions:
            productionRule += condition['key'] + " " + condition['operator'] + " " + condition['value'] + " AND "

        productionRule = "".join(productionRule.rsplit(" AND ", 1))
        productionRule += " THEN " + self.conclusion

        productionRule += " ("

        if (not (self.conditionsMatched == ["root"] or self.conditionsMatched == [])):
            productionRule2 = " IF "
            for condition in self.conditionsMatched:
                # print(condition)
                productionRule2 += condition['key'] + " " + condition['operator'] + " " + condition['value'] + " AND "

            productionRule2 = "".join(productionRule2.rsplit(" AND ", 1))
            productionRule2 += " THEN " + self.conclusion
            productionRule += productionRule2

        # for condition in self.conditionsMatched:
        #     productionRule += str(condition) + " AND "

        productionRule += ")"
        print(productionRule)
        if len(self.children) > 0:
            for child in self.children:
                child.printNode(separatorStr + separatorStr)

    def getNodeAsString(self, separatorStr):
        productionRule = separatorStr + " IF "
        for condition in self.conditions:
            productionRule += condition['key'] + " " + condition['operator'] + " " + condition['value'] + " AND "

        productionRule = "".join(productionRule.rsplit(" AND ", 1))
        productionRule += " THEN " + self.conclusion

        productionRule += " ("

        if (not (self.conditionsMatched == ["root"] or self.conditionsMatched == [])):
            productionRule2 = " IF "
            for condition in self.conditionsMatched:
                # print(condition)
                productionRule2 += condition['key'] + " " + condition['operator'] + " " + condition['value'] + " AND "

            productionRule2 = "".join(productionRule2.rsplit(" AND ", 1))
            productionRule2 += " THEN " + self.conclusion
            productionRule += productionRule2

        # for condition in self.conditionsMatched:
        #     productionRule += str(condition) + " AND "

        productionRule += ")\r\n"
        # print(productionRule)
        if len(self.children) > 0:
            for child in self.children:
                productionRule += child.getNodeAsString(separatorStr + separatorStr)

        return productionRule;

class Tree(object):
    def __init__(self):
        self.root = Node('No Disease', [{'key': '1', 'operator': '=', 'value': '1'}], [])

    def addRuleNode(self, root, ruleDict):
        if not root:
            root = self.root

        if ruleDict['conclusion'] == root.conclusion:
            r_maxConditionsMatched = 0
            maxConditionsMatched = 0
            maxConditions = []
            r_ruleRootConditionArray = self.convertConditionsToStringArray(root.conditions)
            r_ruleDictConditionArray = self.convertConditionsToStringArray(ruleDict['conditions'])
            r_a_b_overlapping = self.checkConditionOverlapping(r_ruleRootConditionArray, r_ruleDictConditionArray)
            r_b_a_overlapping = self.checkConditionOverlapping(r_ruleDictConditionArray, r_ruleRootConditionArray)

            # a_b_difference = self.getConditionOverlapping(root.conditions,ruleDict['conditions'])

            # print("a_b:",r_a_b_overlapping)
            # print("b_a:",r_b_a_overlapping)
            if (0 < len(r_a_b_overlapping) < len(r_ruleRootConditionArray)
                    and
                    r_maxConditionsMatched < (len(r_ruleDictConditionArray) - len(r_a_b_overlapping))):
                maxConditionMatchedNode = root
                r_maxConditionsMatched = len(r_ruleDictConditionArray) - len(r_a_b_overlapping)
                # maxConditions = r_a_b_overlapping

            # Nothing was matched in the parent so skip its children
            if r_maxConditionsMatched < 1 :
                return False;  # No conditions were matched


            # print("******************************")
            for rootChild in root.children:
                ruleNodeConditionArray = self.convertConditionsToStringArray(rootChild.conditions)
                # ruleDictConditionArray = self.convertConditionsToStringArray(ruleDict['conditions'])

                a_b_overlapping = self.checkConditionOverlapping(ruleNodeConditionArray, r_ruleDictConditionArray)
                b_a_overlapping = self.checkConditionOverlapping(r_ruleDictConditionArray, ruleNodeConditionArray)

                # a_b_intersection = self.getConditionOverlapping(rootChild.conditions,ruleDict['conditions'])

                # print("c_a_b:",a_b_overlapping)
                # print("c_b_a:",b_a_overlapping)
                # print("******************************",a_b_overlapping, " == ", b_a_overlapping)
                if (0 < len(a_b_overlapping) < len(ruleNodeConditionArray)
                        and r_maxConditionsMatched < maxConditionsMatched < (
                                len(r_ruleDictConditionArray) - len(a_b_overlapping))):
                    maxConditionMatchedNode = rootChild
                    maxConditionsMatched = len(r_ruleDictConditionArray) - len(a_b_overlapping)
                    # maxConditions = a_b_overlapping

            # if len(self.checkConditionOverlapping(rootChild, ruleDict)) < rootChild.conditions:
            # Check later if this overlapping is equal to or greater than the conditions in rule
            #if maxConditionsMatched > 0:       # No need for this, since the root check will have atleast 1 in it
            conditionsForTree = []

            if r_maxConditionsMatched > maxConditionsMatched:
                b_a_overlapping = r_b_a_overlapping

            for conditionStr in b_a_overlapping:
                strArr = conditionStr.split(":")
                conditionsForTree.append({"key": strArr[0], "operator": strArr[1], "value": strArr[2]})

            self.addRuleAsChild(maxConditionMatchedNode, ruleDict['conclusion'], conditionsForTree, ruleDict['conditions'])

            # maxConditionMatchedNode.children.append(
            #     Node(ruleDict['conclusion'], conditionsForTree, ruleDict['conditions']))
            # self.root.children.append(Node(ruleDict['conclusion'], conditionsForTree, ["root"]))
            return True;

        else:
            isAdded = False
            for rootChild in root.children:
                isAdded = self.addRuleNode(rootChild, ruleDict)
                if isAdded:
                    break
            self.addRuleAsChild(self.root, ruleDict['conclusion'], ruleDict['conditions'], ["root"])
            # self.root.children.append(Node(ruleDict['conclusion'], ruleDict['conditions'], ["root"]))

    def printTree(self):
        self.root.printNode("\t")

    def addRuleAsChild(self, parentNode, ruleConclusion, ruleConditions, supplInfo):
        ruleCondition = self.convertConditionsToStringArray(ruleConditions)
        for nodeChild in parentNode.children:
            nodeChildCondition = self.convertConditionsToStringArray(nodeChild.conditions)
            if len(self.checkConditionOverlapping(nodeChildCondition, ruleCondition)) == 0:
                return
        parentNode.children.append(Node(ruleConclusion, ruleConditions, supplInfo))


    def getTreeAsString(self):
        return self.root.getNodeAsString("\t")

    def convertConditionsToStringArray(self, conditionList):
        conditions = []
        for condition in conditionList:
            conditions.append(condition['key'] + ":" + condition['operator'] + ":" + condition['value'])
        return conditions

    def checkConditionOverlapping(self, aConditionlist, bConditionlist):
        overlapping = set(aConditionlist) - set(bConditionlist)
        return overlapping

    def getConditionOverlapping(self, aConditionlist, bConditionlist):
        return set(aConditionlist).intersection(set(bConditionlist))

    #     #self.data = []
    # def addRule(self, conclusion, rule):
    #     for childRuleFromKB in self.root.children:
    #         if rule['conclusion'] === childRuleFromKB['conclusion']:
    #             childRuleFromKB['conclusion'].children.append()
    # def createChildren(self,amount):
    #     for i in range(0,amount):
    #         self.child.append(Tree())
    # def addRules(self,ruleList):
    #     for rule in ruleList:
    #         self.data.append(rule)

# root = Tree()
# root.createChildren(3)
# root.setChildrenValues([5,6,7]) 
#  root.child[0].createChildren(2)
# root.child[0].setChildrenValues([1,2])
#  # print some values in the tree
# print(root.data[0])
# print(root.child[0].data[0])
