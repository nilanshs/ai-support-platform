# AI Powered Customer Experience Support Platform

This project is a prototype of an AI-powered customer support platform designed to unify customer interactions across multiple channels such as voice, WhatsApp, email, and web chat.

The system analyzes incoming customer messages to understand intent, detect sentiment, predict urgency, and recommend the next best action for support teams.

---

## Key Features

- Intent detection from customer messages
- Sentiment analysis to understand customer mood
- Urgency prediction based on sentiment and keywords
- Customer history lookup for personalization
- Knowledge retrieval for automated responses
- Recommended support actions for agents

---

## System Architecture
# AI Powered Customer Experience Support Platform

This project is a prototype of an AI-powered customer support platform designed to unify customer interactions across multiple channels such as voice, WhatsApp, email, and web chat.

The system analyzes incoming customer messages to understand intent, detect sentiment, predict urgency, and recommend the next best action for support teams.

---

## Key Features

- Intent detection from customer messages
- Sentiment analysis to understand customer mood
- Urgency prediction based on sentiment and keywords
- Customer history lookup for personalization
- Knowledge retrieval for automated responses
- Recommended support actions for agents

---

## System Architecture

The platform consists of multiple modules:

Customer Message
↓
Intent Detection Model
↓
Sentiment Analysis
↓
Urgency Prediction
↓
Customer History Lookup
↓
Knowledge Retrieval (RAG)
↓
Next Best Action Engine
↓
Support Recommendation

-----

## Tech Stack

- Python
- FastAPI
- HuggingFace Transformers
- PyTorch
- FAISS
- Scikit-learn
- Pandas

----

## Project Structure

ai-support-platform
│
├── app.py
├── intent_model.py
├── sentiment_model.py
├── urgency_model.py
├── rag_engine.py
├── actions.py
├── customer_db.py
└── requirements.txt

----

## Running the Prototype

Install dependencies:

pip install -r requirements.txt
Start the FastAPI server:
python -m uvicorn app:app --reload
Once the server starts, open the API interface in your browser: http://127.0.0.1:8000/docs
The interactive FastAPI documentation allows you to test the API endpoints directly.

---

## Example Request

Example input:

customer_id: 1001
message: I want a refund for my order

Example response:

intent: anger
sentiment: negative
urgency_score: 8
recommended_action: Escalate to senior support agent
suggested_response: A support agent will assist you shortly.


---

## Objective of the Prototype

The objective of this project is to demonstrate how AI can help businesses deliver a unified customer experience by:

- Reducing response times
- Improving support accuracy
- Personalizing interactions using customer data
- Automating support workflows

This prototype represents a simplified architecture that can be extended into a full-scale multi-channel customer support platform.

---

## Author

Nilansh Singh  
B.Tech – Mechatronics and Automation Engineering  
IIIT Bhagalpur
