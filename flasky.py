from flask import Flask, request
from flask_cors import cross_origin
import spacy
app = Flask(__name__)
nlp = spacy.blank("en")
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
    return doc.text
    # for token in doc:
    #     print(token.text, token.pos_)
    # return "bye"
