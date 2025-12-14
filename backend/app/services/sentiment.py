def analyze_sentiment(text: str) -> str:
    text = text.lower()

    positive_words = [
        "bagus", "baik", "mantap", "cepat", "puas", "recommended", "keren"
    ]

    negative_words = [
        "jelek", "buruk", "lama", "lambat", "kecewa", "parah", "rusak", "kurang"
    ]

    positive_score = 0
    negative_score = 0

    for word in positive_words:
        if word in text:
            positive_score += 1

    for word in negative_words:
        if word in text:
            negative_score += 1

    if positive_score > negative_score:
        return "positive"
    elif negative_score > positive_score:
        return "negative"
    else:
        return "neutral"
