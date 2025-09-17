def doc_to_choice(doc):
    return doc['elements'] 

def doc_to_text(doc):
    return f"{', '.join(doc['elements'])}:"

def doc_to_target(doc):
    return str(doc['target'])