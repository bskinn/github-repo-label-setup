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

    HEADERS = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {PAT}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    API_URL_BASE = f"https://api.github.com/repos/{repo}/labels"

    labelsets = json.loads(Path("labels.json").read_text())

    for labelset in labelsets:
        set_name = labelset["name"]
        color = labelset["color"]
        labels = labelset["labels"]

        for label in labels:
            label_name = f"{set_name}: {label['name']} {label['icon']}"

            get_resp = rq.get(
                API_URL_BASE + f"/{label_name}",
                headers=HEADERS,
            )

            if get_resp.ok:
                # Label found, so let's update in place
                resp = rq.patch(
                    API_URL_BASE + f"/{label_name}",
                    headers=HEADERS,
                    data=json.dumps(
                        {
                            "new_name": label_name,
                            "description": f"{label.get('text', '')}",
                            "color": color,
                        }
                    ),
                )
                action = "updated"
            else:
                # Not found, let's create
                resp = rq.post(
                    API_URL_BASE,
                    headers=HEADERS,
                    data=json.dumps(
                        {
                            "name": label_name,
                            "description": f"{label.get('text', '')}",
                            "color": color,
                        },
                    ),
                )
                action = "created"

            print(
                f"Label '{label_name}' result: {resp.status_code} ({resp.reason}) ({action})"  # noqa: E501
            )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("No user/repo provided as CLI argument!")

    main(repo=sys.argv[1])
