def detect_issues(product):
    issues = []

    # Missing title
    if not product.get("title"):
        issues.append("Missing title")

    # Title too short
    elif len(product.get("title", "")) < 10:
        issues.append("Title too short")

    # Missing category
    if not product.get("category"):
        issues.append("Missing category")

    # Missing image
    if not product.get("image_url"):
        issues.append("Missing image")

    # Invalid price
    if not product.get("price") or product.get("price") <= 0:
        issues.append("Invalid price")

    return issues


def score_product(product):
    score = 100
    issues = detect_issues(product)

    for issue in issues:
        if issue == "Missing title":
            score -= 30
        elif issue == "Title too short":
            score -= 15
        elif issue == "Missing category":
            score -= 20
        elif issue == "Missing image":
            score -= 25
        elif issue == "Invalid price":
            score -= 20

    return max(score, 0)


def evaluate_product(product):
    issues = detect_issues(product)

    score = score_product(product)

    if score >= 80:
        severity = "LOW"
    elif score >= 50:
        severity = "MEDIUM"
    else:
        severity = "HIGH"

    return {
        "product_id": product.get("id"),
        "issues": issues,
        "score": score,
        "severity": severity
    }