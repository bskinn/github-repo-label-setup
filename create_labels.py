import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path

import requests as rq


@dataclass(kw_only=True)
class Label:
    name: str
    icon: str
    text: str = ""


@dataclass(kw_only=True)
class LabelSet:
    name: str
    color: str
    labels: list[Label]


def main(repo: str):
    PAT = os.environ.get("GITHUB_PAT")

    labelsets = json.loads(Path("labels.json").read_text())

    for labelset in labelsets:
        set_name = labelset["name"]
        color = labelset["color"]
        labels = labelset["labels"]

        for label in labels:
            resp = rq.post(
                f"https://api.github.com/repos/{repo}/labels",
                headers={
                    "Accept": "application/vnd.github+json",
                    "Authorization": f"Bearer {PAT}",
                    "X-GitHub-Api-Version": "2022-11-28",
                },
                data=json.dumps(
                    {
                        "name": (
                            label_name := f"{set_name}: {label['name']} {label['icon']}"
                        ),
                        "description": f"{label.get('text', '')}",
                        "color": f"{color}",
                    }
                ),
            )

            print(f"Label '{label_name}' result: {resp.status_code} ({resp.reason})")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("No user/repo provided as CLI argument!")

    main(repo=sys.argv[1])
