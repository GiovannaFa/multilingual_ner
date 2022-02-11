import spacy

#nlp = spacy.load("en_core_web_sm")

def multilingual_ner(text, lang='en'):
  nlp = spacy.load(f"{lang}_core_web_sm")
  doc= nlp(text)
  dicos= list()
  for ent in doc.ents:
    dico= dict()
    dico["text"]= ent.text
    dico["type"]= ent.label_
    dico["start_pos"]= ent.start_char
    dico["end_pos"]= ent.end_char
    dicos.append(dico)
  return dicos
  
if __name__ == "__main__":
  multilingual_ner("Ben Wallace has said relations between London and Moscow have increased to “above zero” following a “constructive and frank discussion” in the Russian defence ministry.")
