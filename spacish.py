import spacy
nlp = spacy.blank("en")
doc = nlp("I love you")
print(doc.text)
