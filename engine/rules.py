ISSUE_DEFINITIONS = {
    "Missing title": {
        "impact": "Severely reduces product discoverability in search and feeds."
    },
    "Title too short": {
        "impact": "Low-quality titles reduce click-through rate and user trust."
    },
    "Missing category": {
        "impact": "Breaks catalog organization and affects ad targeting accuracy."
    },
    "Missing image": {
        "impact": "Strong negative impact on conversion rates in retail feeds."
    },
    "Invalid price": {
        "impact": "Prevents proper ranking and can block ad approval workflows."
    }
}


def detect_issues(product):
    issues = []

    if not product.get("title"):
        issues.append("Missing title")
    elif len(product.get("title", "")) < 10:
        issues.append("Title too short")

    if not product.get("category"):
        issues.append("Missing category")

    if not product.get("image_url"):
        issues.append("Missing image")

    if not product.get("price") or product.get("price") <= 0:
        issues.append("Invalid price")

    return issues


def score_product(product):
    score = 100
    issues = detect_issues(product)

    penalties = {
        "Missing title": 30,
        "Title too short": 15,
        "Missing category": 20,
        "Missing image": 25,
        "Invalid price": 20
    }

    for issue in issues:
        score -= penalties.get(issue, 0)

    return max(score, 0)


def evaluate_product(product):
    issues = detect_issues(product)
    score = score_product(product)

    enriched_issues = []

    for issue in issues:
        enriched_issues.append({
            "issue": issue,
            "impact": ISSUE_DEFINITIONS.get(issue, {}).get("impact", "No impact defined")
        })

    if score >= 80:
        severity = "LOW"
    elif score >= 50:
        severity = "MEDIUM"
    else:
        severity = "HIGH"

    return {
        "product_id": product.get("id"),
        "score": score,
        "severity": severity,
        "issues": enriched_issues
    }