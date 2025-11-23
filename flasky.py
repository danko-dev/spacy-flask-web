from flask import Flask, request
from flask_cors import cross_origin
import spacy

app = Flask(__name__)

# nlp = spacy.blank("en")
nlp = spacy.load("en_core_web_sm")

@app.route("/")
def home():
    return "hello from flasky"

@app.route("/submit-form", methods=["POST"])
@cross_origin()
def submit_form():
    user_text = request.form.get("text")
    if user_text is None:
        return "did not got user text"
    else:
        return analyzeNlp(user_text)

def analyzeNlp(user_text):
    doc = nlp(user_text)
    tokens = [{
    "text": token.text, 
    "pos": token.pos_, 
    "dep": token.dep_,
    "lemma": token.lemma_,
    } for token in doc]
    return {"tokens": tokens}
    # return doc.text
    # for token in doc:
    #     print(token.text, token.pos_)
    # return "bye"
