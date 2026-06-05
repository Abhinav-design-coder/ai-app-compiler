import json
import os


def save_metrics(
    total,
    successful,
    failed,
    success_rate,
    repair_count,
    avg_latency
):

    results = {
        "total_prompts": total,
        "successful": successful,
        "failed": failed,
        "success_rate": success_rate,
        "repair_count": repair_count,
        "avg_latency_ms": avg_latency
    }

    current_dir = os.path.dirname(os.path.abspath(__file__))
    results_path = os.path.join(current_dir, "evaluation_results.json")

    with open(results_path, "w") as file:

        json.dump(
            results,
            file,
            indent=4
        )