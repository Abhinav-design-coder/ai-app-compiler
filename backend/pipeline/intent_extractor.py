from schemas.intent_schema import Intent


def extract_intent(prompt: str):

    prompt = prompt.lower()

    entities = []
    features = []

    if "contact" in prompt:
        entities.append("contacts")

    if "dashboard" in prompt:
        features.append("dashboard")

    if "payment" in prompt:
        features.append("payments")

    return Intent(
        entities=entities,
        roles=["admin", "user"],
        features=features,
        authentication=True,
        payments="payment" in prompt
    )