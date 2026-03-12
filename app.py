from fastapi import FastAPI
from intent_model import detect_intent
from sentiment_model import detect_sentiment
from urgency_model import predict_urgency
from rag_engine import retrieve_info
from actions import next_action
from customer_db import get_customer

app = FastAPI()

@app.post("/support")

def process_message(customer_id: str, message: str):

    customer = get_customer(customer_id)

    intent = detect_intent(message)
    sentiment = detect_sentiment(message)

    urgency = predict_urgency(sentiment["label"], message)

    info = retrieve_info(intent["label"])

    action = next_action(intent["label"], urgency)

    return {
        "customer": customer,
        "intent": intent,
        "sentiment": sentiment,
        "urgency_score": urgency,
        "recommended_action": action,
        "suggested_response": info
    }