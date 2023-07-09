from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

# chatterbot lib bug fix
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


#create chatbot instance
chatbot = ChatBot("Buddy of Python", tagger_language=ENGSM)

trainer = ListTrainer(chatbot)

# Load intents from JSON
with open('corpus_list.json', 'r') as file:
    intents_data = json.load(file)

# Extract intents from JSON
intents = intents_data['intents']

# Extract patterns and responses and train the chatbot with them
for intent in intents:
    patterns = intent['patterns']
    responses = intent['responses']
    for pattern in patterns:
        trainer.train([pattern] + responses)



while True:
    query = input("You: ")
    response = chatbot.get_response(query)
    print("ChatBot: ", response)
