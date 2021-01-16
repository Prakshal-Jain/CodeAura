# from translate import Translator


# translator= Translator(to_lang="it")
# translation = translator.translate("This is a pen.")

# print(translation)


# def Translate()

import http.client


def Translate(destinationLang: str, userStr: str):
    conn = http.client.HTTPSConnection("microsoft-translator-text.p.rapidapi.com")

    payload = "[\r{\r\"Text\": \""+userStr+"\"\r}\r]"

    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "d15cb7a0bbmsh95063875d7c71f4p14d8ffjsn696853778b90",
        'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com"
    }

    # input text from user goes into the request
    conn.request("POST", "/translate?to="+destinationLang+"&api-version=3.0&profanityAction=NoAction&textType=plain",
                 payload, headers)

    res = conn.getresponse()
    data = res.read()

    # This is a JSON data. Use json.load to get the contents.
    return data.decode("utf-8")

def getLanguages():
    conn = http.client.HTTPSConnection("microsoft-translator-text.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "d15cb7a0bbmsh95063875d7c71f4p14d8ffjsn696853778b90",
        'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com"
    }

    conn.request("GET", "/languages?api-version=3.0", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # This is a JSON data. Use json.load to get the contents.
    return data.decode("utf-8")
