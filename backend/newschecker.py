def check_news_validity(data):
    """
    Simulate AI logic to verify disaster news:
    - Accepts data with type, location, timestamp, etc.
    - Generates a fake confidence score (0 to 1)
    - Flags valid if score > 0.75
    """
    import random

    disaster_type = data.get("type")
    location = data.get("location")
    source = data.get("source")  # e.g., Reuters, UN API

    confidence = round(random.uniform(0.6, 0.99), 2)  # Simulate AI confidence score

    return {
        "disaster": disaster_type,
        "location": location,
        "source": source,
        "confidence": confidence,
        "is_valid": confidence > 0.75
    }
