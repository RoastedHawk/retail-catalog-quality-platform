from data.sample_catalog import sample_catalog
from engine.rules import evaluate_product


def run_catalog_evaluation(catalog):
    results = []

    for product in catalog:
        results.append(evaluate_product(product))

    return {
        "total_products": len(catalog),
        "results": results
    }


if __name__ == "__main__":
    report = run_catalog_evaluation(sample_catalog)

    print("\n=== CATALOG QUALITY REPORT ===\n")
    print(f"Total Products: {report['total_products']}\n")

    for r in report["results"]:
        print(f"Product ID: {r['product_id']}")
        print(f"Score: {r['score']}")
        print(f"Severity: {r['severity']}")
        print(f"Issues: {r['issues']}")
        print("-" * 40)