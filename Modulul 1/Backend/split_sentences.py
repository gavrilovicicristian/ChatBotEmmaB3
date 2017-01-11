import json

def load_json(filepath):
    questions = []
    answers = []
    with open(filepath) as data_file:
        data = json.load(data_file)
    for question in data["questions"]:
        questions.append(question)
    for answer in data["answers"]:
        answers.append(answer)
    return questions, answers

def respond(kernel, sentences, id):
    big_answer = ""
    #procesare sentences --
    questions = load_json("split_sentnces.json")
    for q in questions:
        big_answer = big_answer + " " + kernel.respond(q, id)
    return big_answer
q,a = load_json("split_sentences.json")

