from transformers import pipeline

intent_classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion"
)

def detect_intent(message):
    result = intent_classifier(message)[0]
    return result