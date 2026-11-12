import json
from pathlib import Path

import requests


def verify_build():

    artifact = Path("dist/build-info.json")

    if not artifact.exists():
        raise FileNotFoundError("Build artifact is missing.")

    data = json.loads(artifact.read_text(encoding="utf-8"))

    assert data["service"] == "inventory-api"
    assert data["version"] == "2.0"
    assert data["status"] == "ready"

    # Prepare a request without making an internet call.
    prepared = requests.Request(
        "GET",
        "https://example.com/health"
    ).prepare()

    assert prepared.method == "GET"

    print(f"Requests version: {requests.__version__}")
    print("Application artifact verified.")
    print("HTTP client smoke check passed.")
    print("CI validation successful.")


if __name__ == "__main__":
    verify_build()