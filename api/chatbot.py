# importing the libraries
import torch
import numpy as np
import pickle
from torch import nn
import json
import random
import nltk
from nltk.stem import PorterStemmer

#download stopwords
nltk.download("stopwords")

# neural network
output_targets = 6
vocabulary_size = 64


class chatbot(nn.Module):
    def __init__(self,output_targets,vocabulary_size):
        super(chatbot,self).__init__()
        
        # embedding layer
        self.embedding1 = nn.Embedding(vocabulary_size,15)
        
        # lstm
        self.lstm = nn.LSTM(input_size=15,hidden_size=10,batch_first=True,num_layers=1)

        # fully connected
        self.fc1 = nn.Linear(in_features=10,out_features=output_targets)

    def forward(self,x):
        x = self.embedding1(x)
        x,_ = self.lstm(x)
        x = torch.relu(x[:,-1])
        x = self.fc1(x)
        return x

# working of the chatbot
def predict(some_text):


    #encoding dictionary
    encoding_dict = pickle.load(open("encoding_dict.bin","rb"))

    #encode the input
    some_text = some_text.lower()
    ps = PorterStemmer()
    encoded_text = []
    for word in some_text.split(' '):
        for j in range(len(encoding_dict['words'])):
            if ps.stem(word) == encoding_dict['words'][j]:
                encoded_text.append(encoding_dict['encoding'][j])
                break
    encoded_text = torch.tensor(encoded_text).reshape(1,-1)

    # loading the model and making predictions
    model = chatbot(output_targets,vocabulary_size)
    model.load_state_dict(torch.load("chatbot.pt"))
    y_pred = model(encoded_text).argmax()


    # response
    label_list = ['goodbye', 'greeting', 'location', 'menu', 'reservation','timings']
    label = label_list[y_pred]
    with open("content.json") as file:
        contents = json.load(file)

    for tags in contents['intents']:
        if label == tags['tag']:
            random_number = random.randint(0,len(tags['responses'])-1)
            return (tags['tag'],tags['responses'][random_number])
