# English → Irish
EN_TO_GA = {
    "science/technology": "eolaíocht/teicneolaíocht",
    "travel": "taisteal",
    "politics": "polaitíocht",
    "sports": "spóirt",
    "health": "sláinte",
    "entertainment": "siamsaíocht",
    "geography": "tíreolaíocht"
}

def map_to_irish(doc: str) -> str:
    """Map English category to Irish (gle_Latn)."""
    return EN_TO_GA.get(doc['category'], "unknown")


# English → Basque
EN_TO_EUS = {
    "science/technology": "zientzia/teknologia",
    "travel": "bidaiak",
    "politics": "politikak",
    "sports": "kirolak",
    "health": "osasuna",
    "entertainment": "dibertsioa",
    "geography": "geografia"
}

def map_to_basque(doc: str) -> str:
    """Map English category to Basque (eus_Latn)."""
    return EN_TO_EUS.get(doc['category'], "unknown")


# English → Chinese
EN_TO_ZH = {
    "science/technology": "科学/技术",
    "travel": "旅行",
    "politics": "政治",
    "sports": "体育",
    "health": "健康",
    "entertainment": "娱乐",
    "geography": "地理"
}

def map_to_chinese(doc: str) -> str:
    """Map English category to Chinese (zh_Hans)."""
    return EN_TO_ZH.get(doc['category'], "unknown")