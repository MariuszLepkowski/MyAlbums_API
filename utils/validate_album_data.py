def validate_put_data(data):
    if not data:
        return {"error": "No input data provided"}

    required_fields = ("artist", "title")
    missing_keys = [key for key in required_fields if key not in data]
    empty_values = [key for key in required_fields if not data.get(key)]

    if missing_keys:
        return {"error": f"Missing keys: {', '.join(missing_keys)}"}

    if empty_values:
        return {"error": f"Empty values for: {', '.join(empty_values)}"}

    return None

def validate_patch_data(data):
    if not data:
        return {"error": "No input data provided"}

    allowed_fields = {"artist", "title"}
    unknown_fields = [k for k in data if k not in allowed_fields]
    if unknown_fields:
        return {"error": f"Unknown fields: {', '.join(unknown_fields)}"}

    empty_values = [key for key in data if not data.get(key)]
    if empty_values:
        return {"error": f"Empty values for: {', '.join(empty_values)}"}

    return None
