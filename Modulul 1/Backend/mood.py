import json
import requests

url = 'https://watson-api-explorer.mybluemix.net/tone-analyzer/api/v3/tone?version=2016-05-19'
headers = {'content-type': 'application/json'}

class Mood:

    def get_current_mood(self,message):
        maxValue = 0
        returnedKey = ''
        data = {'text': message}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        jsonResponse = json.loads(response.content)
        try:
            for tone in jsonResponse["document_tone"]["tone_categories"]:
                for i in tone["tones"]:
                    key = i["tone_name"]
                    value = i["score"]
                    if(value > maxValue):
                        returnedKey = key
                        maxValue = value
        except KeyError:
            pass

        return returnedKey
