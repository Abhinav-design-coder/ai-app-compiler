def generate_schemas(intent, architecture):

    database = {
        "tables": [
            {
                "name": "users",
                "fields": [
                    "id",
                    "email",
                    "password",
                    "role"
                ]
            }
        ]
    }

    if "contacts" in intent.entities:
        database["tables"].append({
            "name": "contacts",
            "fields": [
                "id",
                "name",
                "phone"
            ]
        })

    api = {
        "endpoints": [
            {
                "path": "/login",
                "method": "POST"
            }
        ]
    }

    if "contacts" in intent.entities:
        api["endpoints"].append({
            "path": "/contacts",
            "method": "GET"
        })

    ui = {
        "pages": [
            {
                "name": "Login"
            }
        ]
    }

    for module in architecture["modules"]:
        ui["pages"].append({
            "name": module.title()
        })

    auth = {
        "roles": [
            {
                "name": "admin",
                "permissions": [
                    "full_access"
                ]
            },
            {
                "name": "user",
                "permissions": [
                    "basic_access"
                ]
            }
        ]
    }

    return {
        "database": database,
        "api": api,
        "ui": ui,
        "auth": auth
    }