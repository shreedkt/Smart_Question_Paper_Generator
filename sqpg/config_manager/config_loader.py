import json
from pathlib import Path


def load_configuration():
    """
    Load application configuration.

    Returns
    -------
    dict
        Configuration dictionary.
    """

    config_path = Path("config") / "settings.json"

    try:

        with open(config_path, "r", encoding="utf-8") as file:
            configuration = json.load(file)

        return configuration

    except FileNotFoundError:

        print("Error: settings.json not found.")

        return None

    except json.JSONDecodeError:

        print("Error: Invalid JSON format.")

        return None