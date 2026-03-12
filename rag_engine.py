knowledge_base = {
    "refund": "Refund requests can be made within 7 days of delivery.",
    "delivery": "Standard delivery time is usually 3 to 5 business days.",
    "cancel": "Orders can be cancelled before they are shipped."
}

def retrieve_info(intent):

    if "refund" in intent.lower():
        return knowledge_base["refund"]

    if "delivery" in intent.lower():
        return knowledge_base["delivery"]

    if "cancel" in intent.lower():
        return knowledge_base["cancel"]

    return "A support agent will assist you shortly."