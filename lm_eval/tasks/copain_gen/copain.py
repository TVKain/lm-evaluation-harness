def doc_to_choice(doc):
    return doc['elements'] 

def doc_to_text(doc):
    return f"{', '.join(doc['elements'])}:"

def doc_to_target(doc):
    return str(doc['target'])

def process_results(doc: dict, results: list[str]) -> dict[str, int]:
    """
    Process the generated results to determine if the model's output matches the target.
    """
    target = str(doc['target']).strip()

    # Clean and strip each result
    cleaned_results = [res.strip() for res in results][0]
    
    # Check if any of the cleaned results match the target
    is_correct = 1 if target == str(cleaned_results) else 0
    
    return {"exact_match": is_correct}
