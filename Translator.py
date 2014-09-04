#goslate is an api that provides text translation

import goslate

class Translator:

	def __init__(self, desiredLanguage):
		self.desiredLanguage = desiredLanguage
		self.goSlateTranslator = goslate.Goslate()

	def translate(self, stringToTranslate):

		result = stringToTranslate

		#if the string is not the default language, translate it
		if self.detect(stringToTranslate) != self.desiredLanguage:
			#translate the string
			result = self.goSlateTranslator.translate(stringToTranslate, self.desiredLanguage)

		return result

	def detect(self, stringToDetect):
		return self.goSlateTranslator.detect(stringToDetect)
