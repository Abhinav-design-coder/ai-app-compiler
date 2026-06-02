def validate_schemas(schemas):

    errors = []

    database = schemas["database"]
    api = schemas["api"]
    ui = schemas["ui"]
    auth = schemas["auth"]

    # Rule 1
    if len(database["tables"]) == 0:
        errors.append("No database tables found")

    # Rule 2
    if len(api["endpoints"]) == 0:
        errors.append("No API endpoints found")

    # Rule 3
    if len(ui["pages"]) == 0:
        errors.append("No UI pages found")

    # Rule 4
    roles = [r["name"] for r in auth["roles"]]

    if "admin" not in roles:
        errors.append("Admin role missing")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }