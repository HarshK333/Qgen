def pronoun(txt,nlp):
    doc = nlp(txt)
    doc1 = doc._.coref_resolved
    return doc1