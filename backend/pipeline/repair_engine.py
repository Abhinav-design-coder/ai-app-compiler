def repair_schemas(schemas, errors):

    repairs = []

    for error in errors:

        if error == "Admin role missing":

            schemas["auth"]["roles"].append({
                "name": "admin",
                "permissions": [
                    "full_access"
                ]
            })

            repairs.append(
                "Added admin role"
            )

        if error == "User role missing":

            schemas["auth"]["roles"].append({
                "name": "user",
                "permissions": [
                    "basic_access"
                ]
            })

            repairs.append(
                "Added user role"
            )

        if "Missing API endpoint:" in error:

            endpoint_path = error.split("Missing API endpoint: ")[1]

            schemas["api"]["endpoints"].append({
                "path": endpoint_path,
                "method": "GET"
            })

            repairs.append(
                f"Added API endpoint: {endpoint_path}"
            )

        if "Missing UI page for module:" in error:

            module_name = error.split("Missing UI page for module: ")[1]

            schemas["ui"]["pages"].append({
                "name": module_name.title()
            })

            repairs.append(
                f"Added UI page for module: {module_name}"
            )

    return {
        "schemas": schemas,
        "repairs": repairs
    }
