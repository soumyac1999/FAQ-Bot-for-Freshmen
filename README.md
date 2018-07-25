# SoC_2018-FAQ_Bot_for_Freshmen

## Contents

### Folders
- model folder
  - This folder contains the entire dataset collected by me as a `json` file as required by [`rasa-nlu`](https://nlu.rasa.com/index.html)
  - The dataset is a collection of questions asked by students before their admission to IIT Bombay on the [Student Mentor Program Page](http://smp.iitb.ac.in/)
  - The raw dataset is available [here](https://docs.google.com/document/d/1iW_m7Jtr_J4rVu5qPWgf0IAIep7-Q23b6jtW4mwQLy8/edit?usp=sharing)
  - The dataset was prepared using [`tracy`](https://yuukanoo.github.io/tracy/#/agents) which is GUI for creating `json` datasets for chatbots
  - It is available in the [`training_data.json`](https://github.com/soumyac1999/SoC_2018-FAQ_Bot_for_Freshmen/blob/master/model/training_data.json) file
  - The remaining files in this folder were created by [`rasa-nlu`](https://nlu.rasa.com/index.html) engine
- static and templates folder
  - This contains the front end `html` and `css` scripts for the chatbot interface. This was created by my mentor Saurabh Kumar.
  
### Main Files
- nlu.py
  - This is the most important part of our chatbot.
  - It contains our Natural Language Understanding Engine which was made using `rasa-nlu`
  - It uses [`spacy`](https://spacy.io/) at its heart. SpaCy is a free open-source library for Natural Language Processing in Python.
  - Given a query sentence, the model preforms multi-class classification into 18 different classes/intents.
- response_dict.py
  - This is used to preform a one-to-one mapping from the classes to a specific reply.
  - We plan to extend this by using small neural networks which will map the intent and entities returned by the NLU to a set of more specific answers
  - We plan to implement this using [`keras`](https://keras.io/). For this I learnt Keras and implemented a Neural Network on Keras to classify digits from MNIST dataset. The repo can be found [here](https://github.com/soumyac1999/keras-mnist-nn).
  - Due to time constraints, this could not be achieved but I plan to complete this in the future.
- chatbot2.py
  - This file creates a [`flask`](http://flask.pocoo.org/) server for handling the queries from the frontend.
  - It also starts the nlu, loads the model and makes the backend ready for classifying any query.
  - It uses the nlu.py and response_dict.py files to reply to the queries.
  - This is our older chatbot version.
- chatbot.py
  - This is the latest version of our chatbot.
  - It has an added login interface which allows multiple users and stimultaneous logins in addition to all the features of our older model. 
