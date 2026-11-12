import json
from pathlib import Path

from app import build_metadata


def build_application():

    output_dir = Path("dist")
    output_dir.mkdir(exist_ok=True)

    artifact = output_dir / "build-info.json"

    artifact.write_text(
        json.dumps(build_metadata(), indent=4),
        encoding="utf-8"
    )

    print("Build completed successfully.")
    print(f"Generated artifact: {artifact}")


if __name__ == "__main__":
    build_application()