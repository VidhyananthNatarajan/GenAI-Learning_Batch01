# Parts of speech tagging and NER - Named Entity Recognition  - Library Spacy
import spacy

# Load spacy English Model
nlp = spacy.load("en_core_web_sm")

# Sample text
text ="Apple is looking to buy few of the startup based out of U.K and trying to setup some offices in Europe by 2027."

# Process the text
processed_doc = nlp(text)

# POS Tagging
print("Part of Speech Taging")
for token in processed_doc:
    print(f"{token.text}:{token.pos_} ({token.tag_})")

# Named Entity recognition
print("\n Named Entity REcognition")
for enti in processed_doc.ents:
    print(f"{enti.text}:{enti.label_} --> ({spacy.explain(enti.label_)})")    