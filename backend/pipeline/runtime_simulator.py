def simulate_runtime(schemas):

    issues = []

    if not schemas["database"]["tables"]:
        issues.append("Database missing")

    if not schemas["api"]["endpoints"]:
        issues.append("API missing")

    if not schemas["ui"]["pages"]:
        issues.append("UI missing")

    if not schemas["auth"]["roles"]:
        issues.append("Auth missing")

    return {
        "deployable": len(issues) == 0,
        "issues": issues
    }
