def validate_module_pages(architecture, schemas):

    errors = []

    modules = architecture["modules"]

    pages = [
        page["name"].lower()
        for page in schemas["ui"]["pages"]
    ]

    ignored_modules = ["auth"]

    for module in modules:

        if module.lower() in ignored_modules:
            continue

        if module.lower() not in pages:
            errors.append(
                f"Missing UI page for module: {module}"
            )

    return errors


def validate_entity_apis(intent, schemas):

    errors = []

    endpoints = [
        endpoint["path"]
        for endpoint in schemas["api"]["endpoints"]
    ]

    for entity in intent.entities:

        expected = f"/{entity}"

        if expected not in endpoints:
            errors.append(
                f"Missing API endpoint: {expected}"
            )

    return errors


def validate_roles(schemas):

    errors = []

    roles = [
        role["name"]
        for role in schemas["auth"]["roles"]
    ]

    if "admin" not in roles:
        errors.append(
            "Admin role missing"
        )

    if "user" not in roles:
        errors.append(
            "User role missing"
        )

    return errors


def validate_schemas(intent, architecture, schemas):

    errors = []

    errors.extend(
        validate_module_pages(
            architecture,
            schemas
        )
    )

    errors.extend(
        validate_entity_apis(
            intent,
            schemas
        )
    )

    errors.extend(
        validate_roles(
            schemas
        )
    )

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }