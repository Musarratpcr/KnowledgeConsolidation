import re
import nltk
import time
import pickle
import os.path
from pathlib import Path
from scipy import spatial
from nltk.tag import StanfordPOSTagger
from sentence_transformers import SentenceTransformer
from termSemanticType import *

class ruleExtractor:

	def __init__(self):

		self.termSemanticTypeObj = TermSemanticType()
		self.verbPOS = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
		self.nounPOS = ['NNP', 'NN']
		self.articlePOS = ['IN', 'TO']
		self.blacklist = ['(', ')', '%', 'mmol/L', 'B', 'kg/m2', '[', ']', 'mg', 'Hg']

	def getSentences(self, text):

		sentences = nltk.sent_tokenize(text)

		return sentences

	def getPOSTagging(self, sentences):

		stanford_dir = "Data/stanford-postagger-full-2018-10-16"
		modelfile = stanford_dir+"/models/english-bidirectional-distsim.tagger"
		jarfile = stanford_dir+"/stanford-postagger.jar"
		tagger=StanfordPOSTagger(model_filename=modelfile, path_to_jar=jarfile)

		posTaggedSentences = []

		for sent in sentences:
			tokens = nltk.word_tokenize(sent)
			tokensPOS = tagger.tag(tokens)
			posTaggedSentences.append(tokensPOS)

		return posTaggedSentences

	def generateTripelFromArray(self, nouns1, verb, nouns2):

		triples = []
		for noun1 in nouns1:
			for noun2 in nouns2:
				triples.append([noun1, verb[0], noun2])
		return triples

	def readPickleFile(self, url):

		filehandler = open(url, 'rb')
		data = pickle.load(filehandler)
		
		return data

	def writePickle(self, url, data):

		pickle.dump( data, open( url, "wb" ) )

	def getTripples(self, baseURL, text):

		triplesFile = baseURL+'triples.pb'
		
		file = Path(triplesFile)
		if file.exists():
			triples = self.readPickleFile(triplesFile)
		else:
			sentences = self.getSentences(text)
			posTaggedSentences = self.getPOSTagging(sentences)
			triples = []

			for taggedSent in posTaggedSentences:
				nouns1 = []
				verb   = []
				nouns2 = []
				
				for index, taggedToken in enumerate(taggedSent):

					if(taggedToken[1] in self.nounPOS):
						
						if(len(verb) <= 0):
							nouns1.append(taggedToken[0])
						else:
							nouns2.append(taggedToken[0])

					if(taggedToken[1] in self.verbPOS):

						if(len(verb) > 0 and len(nouns1) > 0 and len(nouns2) > 0):

							sentenceTriples = self.generateTripelFromArray(nouns1, verb, nouns2)
							if(len(sentenceTriples) > 0 ):
								triples = triples + sentenceTriples

							nouns1 = []
							verb   = []
							nouns2 = []
							
						if (taggedSent[index + 1][1] in self.articlePOS):
							verb.append(taggedToken[0] + ' ' + taggedSent[index + 1][0])
						else:	
							verb.append(taggedToken[0])

				sentenceTriples = self.generateTripelFromArray(nouns1, verb, nouns2)
				
				if(len(sentenceTriples) > 0 ):
					triples = triples + sentenceTriples		
			self.writePickle(triplesFile, triples)

		return triples

	def getUniqueTriples(self, baseURL, triples):

		uniqueTriplesFile = baseURL+'uniqueTriples.pb'
		
		file = Path(uniqueTriplesFile)
		if file.exists():
			uniqueTriples = self.readPickleFile(uniqueTriplesFile)
		else:
			uniqueTriples = []
			for triple in triples:
				if triple not in uniqueTriples:
					uniqueTriples.append(triple)

			self.writePickle(uniqueTriplesFile, uniqueTriples)

		return uniqueTriples

	def getMedicalTriples(self, baseURL, triples):

		medicalTriplesFile = baseURL+'medicalTriples.pb'

		file = Path(medicalTriplesFile)

		if file.exists():
			medicalTriples = self.readPickleFile(medicalTriplesFile)
		else:
			medicalTriples = []
			
			filehandler = open('semanticType.pb', 'rb')
			existingSemanticType = pickle.load(filehandler)
			
			updateExistingSemantic = 0

			for index, triple in enumerate(triples):
				
				if(triple[0] not in self.blacklist and triple[2] not in self.blacklist):

					firstTermExist = 0
					secondTermExist  = 0
					semanticType1 = 'NONE'
					semanticType2 = 'NONE'

					for existingSemantic in existingSemanticType:

						if existingSemantic[0] == triple[0].lower():
							semanticType1 = existingSemantic[1]
							firstTermExist = 1

						if existingSemantic[0] == triple[2].lower():
							semanticType2 = existingSemantic[1]
							secondTermExist = 1

						if (firstTermExist == 1 and secondTermExist == 1):
							break

					if (firstTermExist == 0):
						semanticType1 = self.termSemanticTypeObj.getTermSemanticType(triple[0])
						updateExistingSemantic = 1
						existingSemanticType.append([triple[0].lower(), semanticType1])
					
					if (secondTermExist == 0):
						semanticType2 = self.termSemanticTypeObj.getTermSemanticType(triple[2])
						updateExistingSemantic = 1
						existingSemanticType.append([triple[2].lower(), semanticType2])

					if(semanticType1 != 'NONE' or semanticType2 != 'NONE'):
						medicalTriples.append(triple)

					if (index % 10 == 0):
						if updateExistingSemantic == 1 and len(existingSemanticType) > 0:
							pickle.dump( existingSemanticType, open( "semanticType.pb", "wb" ) )
							file = open('semanticType.pb', 'rb')
							existingSemanticType = pickle.load(file)
							updateExistingSemantic = 0

			self.writePickle(medicalTriplesFile, medicalTriples)

			
		return medicalTriples

	def triplestoSting(self, triples):
		tripleString = []

		for triple in triples:
			tripleString.append(triple[0]+' '+ triple[1]+' ' + triple[2])

		return tripleString

	def getCausalTriples(self, baseURL, triggers, trigger_embeddings, candidate, candidate_embeddings):

		causalTriplesFile = baseURL+'causalTriples.pb'

		file = Path(causalTriplesFile)

		if file.exists():
			print('caulsa triple file exist')
			causalTriples = self.readPickleFile(causalTriplesFile)
		else:
			print('caulsa triple file does not exist')
			causalTriples = []
			
			for cand, candidate_embedding in zip(candidate, candidate_embeddings):
				for sentence, trigger_embedding in zip(triggers, trigger_embeddings):
					similarity = 1 - spatial.distance.cosine(candidate_embedding, trigger_embedding)
					if (similarity) > 0.8 and cand not in causalTriples:
						causalTriples.append(cand)
						break

			self.writePickle(causalTriplesFile, causalTriples)
			
		return causalTriples

	def getCausalTriggers(self):

		triggersFileName = 'TotalUniqueCausalTriple72359.txt'
		triggersFile = Path(triggersFileName)

		if triggersFile.exists():
			print('triggers file exist')
			file = open(triggersFileName, "r")
			triggers = eval(file.read())
		else:
			print('tiggers file not found')
			triggers = []

		return triggers

	def getTriggerEmbeddings(self, triggers):

		triggerEmbeddingsFile = 'triggerEmbeddings.pb'
		file = Path(triggerEmbeddingsFile)

		if file.exists():
			triggerEmbeddings = self.readPickleFile(triggerEmbeddingsFile)
		else:

			model = SentenceTransformer('bert-base-nli-mean-tokens')
			triggerEmbeddings = model.encode(triggers)

			self.writePickle(triggerEmbeddingsFile, triggerEmbeddings)
				
		return triggerEmbeddings

	def getMedicalTripleEmbeddings(self, baseURL, medicalTriples):

		medTripleEmbeddingsFile = baseURL+'medicalTriplesEmbeddings.pb'
		file = Path(medTripleEmbeddingsFile)

		if file.exists():
			medicalTriplesEmbeddings = self.readPickleFile(medTripleEmbeddingsFile)
		else:
			model = SentenceTransformer('bert-base-nli-mean-tokens')
			medicalTriplesEmbeddings = model.encode(medicalTriples)

			self.writePickle(medTripleEmbeddingsFile, medicalTriplesEmbeddings)

		return medicalTriplesEmbeddings

	def extracRules (self, baseURL, sentences, causalTriples):

		rulesFile = baseURL+'rules.pb'
		rules = []
		
		file = Path(rulesFile)
		if file.exists():
			rules = self.readPickleFile(rulesFile)
		else:
			for index, sentence in enumerate(sentences):

				tokens = nltk.word_tokenize(sentence)
				digits = re.findall(r"\d+",sentence)
				
				if len(digits) > 0 :
					
					for causalIndex, triple in enumerate(causalTriples):

						rule = ''
						tripleArray = triple.split()
						tripleExist = True

						for token in tripleArray:
							if(token not in tokens):
								tripleExist = False
								break

						if tripleExist:
							casueIndex = tokens.index(tripleArray[0])

							digitsWithInBound = []

							for digitIndex, digit in enumerate(digits):
								
								if digit in tokens:
									digitIndexInSentence = tokens.index(digit)

									if abs(causalIndex - digitIndexInSentence) < 6:
										digitsWithInBound.append(digit)
							
							if (len(digitsWithInBound) > 0):
								
								if(len(digitsWithInBound) > 1):

									rule = "IF " + tripleArray[0] + " = " + min(digitsWithInBound) + ' - ' + max(digitsWithInBound) + " THEN " + tripleArray[len(tripleArray) - 1]
									
									if(rule not in rules):
										rules.append(rule)
								else : 
									rule = "IF " + tripleArray[0] + " = " + min(digitsWithInBound) + " THEN " + tripleArray[len(tripleArray) - 1]
									if(rule not in rules):
										rules.append(rule)

			self.writePickle(rulesFile, rules)

		return rules


	
	def ShowRules(self, baseURL, fileName):
		
		file = Path(baseURL+fileName)
		if file.exists():
			
			fileHandler = open(baseURL+fileName, "r", encoding="utf8")
			fileText = fileHandler.read()
			
			sentences = self.getSentences(fileText)
			print('Total Sentences: ', len(sentences))

			
			triples = self.getTripples(baseURL, fileText)
			print('total triples: ', len(triples))

			uniqueTriples = self.getUniqueTriples(baseURL, triples)
			print('total unique triples: ', len(uniqueTriples))

			medicalTriples = self.getMedicalTriples(baseURL, uniqueTriples)
			print('Total Medical Triples: ', len(medicalTriples))

			triggers = self.getCausalTriggers()
			print('Total triggers: ', len(triggers))

			triggerEmbeddings = self.getTriggerEmbeddings(triggers)
			print('Total Trigger Embeddings: ', len(triggerEmbeddings))

			medtriples = self.triplestoSting(medicalTriples)
			
			medicalTriplesEmbeddings = self.getMedicalTripleEmbeddings(baseURL, medtriples)
			print('Total medical tripgles Embeddings: ', len(medicalTriplesEmbeddings))

			causalTriples = self.getCausalTriples(baseURL, triggers, triggerEmbeddings, medtriples, medicalTriplesEmbeddings)
			print('Total causal Triples: ', len(causalTriples))
			# print('Causal Tripes as Rules')
			# print(causalTriples)

			rules = self.extracRules(baseURL, sentences, causalTriples)
			print("total Rules: ", len(rules))
			print(rules)

			
						
		else:
			print('file "', url , '" not found')
    	

ruleExtractorObj = ruleExtractor()
ruleExtractorObj.ShowRules('G3/', 'G3.txt')