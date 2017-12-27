from modules import interface as ITF

import nltk
import re
import random
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
from nltk.tag import pos_tag

HELLOWORDS = [ "Hello", "Hi!", "Hi", "Hey!", "Hey", "Hola!", "Hola", "How are you!" ]
BYEWORDS = [ "See you.", "Take care.", "Nice day!", "Bye!", "BR" ]
FINEWORDS = [ "I'm fine thank you", "Fine and you?", "Very well", "Fine, thank you!", "I'm ok, hope you're ok too" ]
STATEVERBS = [ "be", "feel", "seem", "stay" ]

class Robot:
    def __init__(self):
        self.name = "Harvey"
        ITF.say_hello(self.name)
        self.start()
    
    def start(self):
        answer = raw_input()
        self.clean_text(answer)

    def clean_text(self, text):
        results = []
        results2 = []

        #separate sentences if multiple
        sentences = re.split(r'!\s*|\.\s*|\?\s*', text)
        if sentences[-1] == "":
            sentences.pop()

        #tokenization
        for sentence in sentences:
            results.append(word_tokenize(sentence))
        print results
        self.comprehension(results)

    def comprehension(self, list_of_sent):
        results = []
        returned_sent = ""
        for sentence in list_of_sent:
            results.append(pos_tag(sentence))
        print results

        for result in results:
            temp = { k[0]:v[1] for k, v in zip(result, result) }
            print temp
            
            for (word, pos) in result:
                if word.title() in HELLOWORDS:
                    returned_sent += (HELLOWORDS[random.randint(0, len(HELLOWORDS)-1)] + ". ")

            if 'you' in temp.keys():
                if temp['you']=='PRP':
                    if 'WRB' in temp.values() and 'PRP' in temp.values():
                        returned_sent += (FINEWORDS[random.randint(0, len(FINEWORDS)-1)] + ". ")

        returned_sent.strip()
        print returned_sent

robot = Robot()
