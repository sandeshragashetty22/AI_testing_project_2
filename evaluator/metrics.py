
def keyword_score(response, expected_keywords):
    count = 0
    response_lower = response.lower()

    for keyword in expected_keywords:
        if keyword.lower() in response_lower:
            count += 1
    return count / len(expected_keywords)


def forbidden_penalty(response, forbidden_keywords):
    response = response.lower()

    for word in forbidden_keywords:
        if word.lower() in response:
            return 1
    return 0


def tone_score(response):
    polite_words = ["please", "assist", "help", "sorry"]
    response = response.lower()

    count = 0
    for word in polite_words:
        if word in response:
            count += 1

    return count / len(polite_words)