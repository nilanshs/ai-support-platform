customers = {
    "1001": {
        "name": "Rahul",
        "tier": "premium",
        "history": [
            "delivery delay complaint",
            "refund request"
        ]
    }
}

def get_customer(customer_id):
    return customers.get(customer_id)