def predict_urgency(sentiment, message):

    score = 3

    if sentiment == "NEGATIVE":
        score += 3

    urgent_words = ["urgent", "refund", "cancel", "complaint"]

    for word in urgent_words:
        if word in message.lower():
            score += 2

    return min(score, 10)