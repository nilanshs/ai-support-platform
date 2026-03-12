def next_action(intent, urgency):

    if urgency >= 8:
        return "Escalate to senior support agent"

    if "refund" in intent.lower():
        return "Initiate refund workflow"

    if "delivery" in intent.lower():
        return "Provide delivery tracking information"

    return "Assign case to support team"