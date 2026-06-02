def generate_architecture(intent):

    modules = ["auth"]

    modules.extend(intent.entities)
    modules.extend(intent.features)

    return {
        "modules": list(set(modules))
    }