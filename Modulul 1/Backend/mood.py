import json
import requests

url = 'https://watson-api-explorer.mybluemix.net/tone-analyzer/api/v3/tone?version=2016-05-19'
headers = {'content-type': 'application/json'}

class Mood:
    def __init__(self):
        self.moodScores = dict()

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
        try:
            for tone_categories in jsonResponse["document_tone"]["tone_categories"]:
                key = tone_categories['tones'][0]['tone_name']
                value = tone_categories['tones'][0]['score']
                if key in self.moodScores:
                    self.moodScores[key] += value
                else:
                    self.moodScores[key] = value
        except KeyError:
            pass


# m = Mood()
# print("I love you")
# m.addMoodsForMessage("How are you?")
# print('Current mood: ' + m.getCurrentMood())
