# Importing Packages
from flask import Flask, render_template, request
import urllib
import requests
from bs4 import BeautifulSoup
import urllib.request
from translate import translate
from generator_utils import decode, fix_URI

# Loading BertForQuestionAnswering Model and Tokenizer
'''model = BertForQuestionAnswering.from_pretrained('./model')
tokenizer = BertTokenizer.from_pretrained('./tokenizer')
nlp = English()
sentencizer = nlp.create_pipe("sentencizer")
nlp.add_pipe(sentencizer)'''
# desktop user-agent
def brain(question):# defining Segment Ids # converting input_ids into the strings
    answer ='' # Getting most confident answer
    answer = translate(question,"data/art_30")
    answer = answer.replace(" ##", "") # refining answer
    answer = answer.replace("<end>", "")
    return answer

app = Flask(__name__,template_folder='templates')
# starts ngrok when the app is run

# Takes a question about to the given text and returns the answer to the asked question


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    finaltranso = brain(userText)
    finaltranso = decode(finaltranso)
    print("decoded : "+finaltranso)
    finaltranso = fix_URI(finaltranso)
    print("fixed uri : "+finaltranso)
    return finaltranso.replace('<','&lt').replace('>','&gt')

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    app.run(debug=True)
