import yaml
from pathlib import Path
import sys


def translate(path: str) -> dict:
    data = Path(path).read_text(encoding="utf8")
    compose = yaml.safe_load(data)
    for service in compose["services"]:
        for i, env in enumerate(compose["services"][service]["environment"]):
            if "=" not in env:
                compose["services"][service]["environment"][i] = f"{env}=${{{env}}}"
    return compose


if __name__ == "__main__":
    assert len(sys.argv) > 1, "missing file"
    new_compose = translate(sys.argv[1])
    new_data = yaml.safe_dump(new_compose)
    sys.stdout.write(new_data)
    sys.stdout.write("\n")
