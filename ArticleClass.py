import ArticleParser
from bs4 import BeautifulSoup

class Article:
	def __init__(self, articleURL):
		#get dictionary of article info
		self.articleInfo = ArticleParser.parseArticle(articleURL)
		self.parsedArticleContent = None
	def getDomain(self):
		return self.accessArticleInfoDictionary("domain")

	def getArticleURL(self):
		return self.accessArticleInfoDictionary("url")

	def getAuthor(self):
		return self.accessArticleInfoDictionary("author")

	def getWordCount(self):
		return self.accessArticleInfoDictionary("word_count")

	def getTotalPages(self):
		return self.accessArticleInfoDictionary("total_pages")

	def getUnparsedArticleContentHTML(self):
		return self.accessArticleInfoDictionary("content")

	def getParsedArticleContent(self):
		if not self.parsedArticleContent:

			textToParse = self.getUnparsedArticleContentHTML()

			#Cleans up spacing of article
			textToParse = textToParse.replace("<p>", " ")
			textToParse = textToParse.replace("</p>", " ")


			soup = BeautifulSoup(textToParse)
			self.parsedArticleContent = soup.get_text()

		return self.parsedArticleContent



	def accessArticleInfoDictionary(self, key):
		return self.articleInfo[key]