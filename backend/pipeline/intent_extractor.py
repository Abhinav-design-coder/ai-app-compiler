import re
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

    # Dynamic entity detection
    patterns = [
        r"(?:with|manage|create|tracking|database of|list of|for|management of|system for)\s+([a-zA-Z\s,]+)",
        r"([a-zA-Z]+)\s+(?:app|application|system|manager|database)"
    ]
    for pattern in patterns:
        matches = re.finditer(pattern, prompt)
        for match in matches:
            phrase = match.group(1)
            parts = re.split(r",|and|or", phrase)
            for part in parts:
                words = part.strip().split()
                if words:
                    word = words[-1].strip()
                    if word not in ["app", "application", "system", "database", "dashboard", "login", "auth", "payment", "payments", "role", "roles"]:
                        if word.endswith("y"):
                            word = word[:-1] + "ies"
                        elif not word.endswith("s"):
                            word += "s"
                        
                        if word not in entities:
                            entities.append(word)

    if "users" in entities:
        entities.remove("users")

    return Intent(
        entities=entities,
        roles=["admin", "user"],
        features=features,
        authentication=True,
        payments="payment" in prompt
    )