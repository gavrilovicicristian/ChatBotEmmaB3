import aiml,json

def initialize_bot(kernel,id):
    json_data=open('robot_personality.json').read()
    data=json.loads(json_data)
    # kernel.setPredicate("name", data["name"], id)
    for attr in data:
        kernel.setBotPredicate(attr,data[attr])