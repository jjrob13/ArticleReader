import urllib2, json, urllib, MyAPITokens



#returns dictionary of article information
def parseArticle(articleURL):
	apiBaseURL = "http://readability.com/api/content/v1/parser"

	#parameters dictionary
	apiParams = {}

	#add parameters
	apiParams["url"] = articleURL
	apiParams["token"] = READABILITY_API_TOKEN

	#encode params for url
	encodedParams = urllib.urlencode(apiParams)

	fullURL = apiBaseURL + "?" + encodedParams

	#open the url
	urlResponse = urllib2.urlopen(fullURL)

	#return the string response in dictionary format
	return json.loads(urlResponse.read())

