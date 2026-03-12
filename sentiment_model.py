from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def detect_sentiment(message):
    result = sentiment_pipeline(message)[0]
    return result