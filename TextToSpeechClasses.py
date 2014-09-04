from Translator import Translator
import urllib
import MyAPITokens

ENCODING = "utf_8"

#This free api only works for English text
class EngOnlyTTS:
	def __init__(self):
		langaugeToTranslate = "en"
		self.translator = Translator(langaugeToTranslate)
		self.baseAPIURL = "http://tts-api.com/tts.mp3"

	def getAudioFileLink(self, stringToRead):
		#convert to english
		stringToRead = self.translator.translate(stringToRead)

		#encode to utf-8
		stringToRead = stringToRead.encode(ENCODING)

		params = {"q": stringToRead}

		fullAPIURL = self.baseAPIURL + "?" + urllib.urlencode(params)
		return fullAPIURL


##########################################################################
##########################################################################

class VoiceRSSTTS:
	def __init__(self, desiredLanguage = "en-us"):
		self.desiredLanguage = desiredLanguage

		self.translator = Translator(VoiceRSSTTS.convertLangCodeForGoog(desiredLanguage))
		self.baseAPIURL = "http://api.voicerss.org/"

	def getAudioFileLink(self, stringToRead):
		stringToRead = self.translator.translate(stringToRead)

		#encode to utf-8
		stringToRead = stringToRead.encode(ENCODING)
		params = {"key" : VoiceRSSTTS.VOICE_RSS_TTS_API_KEY, "src" : stringToRead, "hl" : self.desiredLanguage}
		fullAPIURL = self.baseAPIURL + "?" + urllib.urlencode(params)

		return fullAPIURL

	@staticmethod
	def convertLangCodeForGoog(langCode):
		langCodeDict = {
		"en-us" : "en",
		"en-ca" : "en",
		"en-au" : "en",
		"en-gb" : "en",
		"en-in" : "en",
		"ca-es" : "ca",
		"zh-cn" : "zh-CN",
		"zh-hk" : "zh-TW",
		"zh-tw" : "zh-TW",
		"da-dk" : "da",
		"nl-nl" : "nl",
		"fi-fi" : "fi",
		"fr-ca" : "fr",
		"fr-fr" : "fr",
		"de-de" : "de",
		"it-it" : "it",
		"ja-jp" : "ja",
		"ko-kr" : "ko",
		"nb-no" : "no",
		"pl-pl" : "pl",
		"pt-br" : "pt",
		"pt-pt" : "pt",
		"ru-ru" : "ru",
		"es-mx" : "es",
		"es-es" : "es",
		"sv-se" : "sv"

		}

		return langCodeDict[langCode]
