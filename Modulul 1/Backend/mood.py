import json
import requests

url = 'https://watson-api-explorer.mybluemix.net/tone-analyzer/api/v3/tone?version=2016-05-19'
headers = {'content-type': 'application/json'}

class Mood:
    def __init__(self):
        self.moodScores = ();

    def getCurrentMood(self):
        auxMoodScore = 0
        currentMood = ""
        for key,value in self.moodScores.items():
            if value > auxMoodScore:
                currentMood = key
                auxMoodScore = value
        return currentMood

    def addMoodsForMessage(self,message):
        data = {'text': message}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        jsonResponse = json.loads(response.content)
        for key,value in jsonResponse["document_tone"].items():
            print (value)

m = Mood()
m.addMoodsForMessage("What's up ?");
