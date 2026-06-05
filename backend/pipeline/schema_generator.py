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

    for entity in intent.entities:
        if entity == "users":
            continue
        
        fields = ["id"]
        if entity == "contacts":
            fields.extend(["name", "phone"])
        elif entity == "products":
            fields.extend(["name", "price", "stock"])
        elif entity == "orders":
            fields.extend(["customer", "total", "status"])
        elif entity == "tasks":
            fields.extend(["title", "description", "completed"])
        else:
            fields.extend(["name", "description"])
            
        database["tables"].append({
            "name": entity,
            "fields": fields
        })

    api = {
        "endpoints": [
            {
                "path": "/login",
                "method": "POST"
            }
        ]
    }

    for entity in intent.entities:
        if entity == "users":
            continue
        api["endpoints"].append({
            "path": f"/{entity}",
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
        page_name = module.title()
        if not any(p["name"] == page_name for p in ui["pages"]):
            ui["pages"].append({
                "name": page_name
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