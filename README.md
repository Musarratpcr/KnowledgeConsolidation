# KnowledgeConsolidation

The repository contains source code and a steps by steps guide to get consolidated knowledge in Ripple Down Rules format. The repository containes two main foder structued  and unstructeud dealing with structured knoweldge acquistion and unstructued knowledge acquistion respectively.

# Structured Knowledge Acquistion

For structued knowledge acquisition we used Rapid Miner white box models (DT, J48, PART, and RIPPER )  to acquired knowledge. The knoweldge acquried for all three datasets used in our study are given in "SSM_DS Extracted Rules Raw", "PID-DS Extracted Rules Raw", and "CHD-DS Extracted Rules Raw" directories, respectively. The acquired knowledge/rules are transform into executable format presetned in "SSMDSRule.py", "PIDDSRules.py", and "CHDDSRules.py", respectively. These rules are initally used to evlaute the indivitual models performance, and later for knowledge combination, and consolidation. 

# Unstructured Knowledge Acquistion
This directory contains the implementation of unstructured kwnowledge acquistion as shown in "ruleExtractor.py" file. It extracts rules from medical textual resrouces. Taking medical text as input, it use existing text preprocessing techniques, to divide text to sentence and tokens. Using Standform POS taggers, it tags each sentence tokens with their corresponding Part of Speech (POS) tag.  This POS tagging is used to extracted triples of the form <Noun, Verb, Noun> from each sentene. The extracted triples are filtered by removed duplicate tripels. The filter tripels are evlauted for bing medical or non-medical triples. To class a triple as medical or non-medical we utalized Unified medical lanague system (UMLS) semantic type. The trems symantic types are fetch via a code in "termSemanticType.py" file. Please note that to use UMLS service, use need to have valid UMLS Profile Key. To reproduce the results please provide your UMLS key in the file "termSemanticType.py". All non-medical tripels are filtered out. A triple have one or more terms sematic type as "NONE" is considered as non-medical triple.

To check the relation between the terms used in the tripel we used causality mining techniques. We have provided a list of 72359 causal triggers "TotalUniqueCausalTriple72359.txt". we generate triggers embeddings using BERT modal embedding techniques. Simialry we genrate embeddings for medical triples as well. To check triple has causal relation, we compare each medical triple embedding with Triggers embedding and find the similarity between them. A  triple having similarity value greater then or equal to 0.8 are considerd as cusal triple. The cuasl triples are then transform to rules to be consolidated to other rules.

For this study, we have utalized three diabetes guides G1, G2, G3, the result of each steps achived is shown in the corresponding folders. 

# Expert Knowledge
We also have acquired expert knoweledge as a flowchat shown in the menuscript The flowchart is transrom to IF conditions THEN Conclustion form as rules.

# Rule Combination 
"rules.py" file combine all the extrated rules. and identifies duplicate and conflect rules presented in the cobmine list. 


# Rule Consolidation
The rule consolidation is done in the RdrTree.py file. The result procduced by the consolidation algorithm is shown in rdrTree.txt. To reproduce the result, user need to run the file rules.py, the RDR tree will be generated and saved to rdrTree.txt file.

The rules acquired by each individual method are consolidate into  RDR models, taking expert into a loop. The realization and detail of the system can be found in http://imprc.cafe24.com/


