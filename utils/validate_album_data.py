def validate_album_data(data):
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