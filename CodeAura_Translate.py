# from translate import Translator


# translator= Translator(to_lang="it")
# translation = translator.translate("This is a pen.")

# print(translation)


# def Translate()

import http.client

def Translate(txtFromUser : str):
	conn = http.client.HTTPSConnection("microsoft-translator-text.p.rapidapi.com")

	payload = "[\r{\r\"Text\": \"I would really like to drive your car around the block a few times.\"\r}\r]"

	headers = {
    	'content-type': "application/json",
    	'x-rapidapi-key': "d15cb7a0bbmsh95063875d7c71f4p14d8ffjsn696853778b90",
    	'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com"
	}

	#input text from user goes into the request
	conn.request("POST", "/translate?to=***txtFromUser***&api-version=3.0&profanityAction=NoAction&textType=plain", payload, headers)

	res = conn.getresponse()
	data = res.read()

	#print(data.decode("utf-8"))

def getLanguages():
	conn = http.client.HTTPSConnection("microsoft-translator-text.p.rapidapi.com")

	headers = {
    	'x-rapidapi-key': "d15cb7a0bbmsh95063875d7c71f4p14d8ffjsn696853778b90",
    	'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com"
    }

	conn.request("GET", "/languages?api-version=3.0", headers=headers)

	res = conn.getresponse()
	data = res.read()

	#print(data.decode("utf-8"))