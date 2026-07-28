import json
import shutil
from pathlib import Path


REGISTRY_PATH = Path("models/registry")


def register_model(

    model_path,

    metrics

):

    REGISTRY_PATH.mkdir(

        parents=True,

        exist_ok=True

    )

    versions = [

        d

        for d in REGISTRY_PATH.iterdir()

        if d.is_dir()

    ]

    version = f"v{len(versions)+1}"

    version_dir = REGISTRY_PATH / version

    version_dir.mkdir()

    shutil.copy(

        model_path,

        version_dir / "best_model.pkl"

    )

    with open(

        version_dir / "metrics.json",

        "w"

    ) as file:

        json.dump(

            metrics,

            file,

            indent=4

        )

    return version