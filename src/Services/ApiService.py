import os
from csv import DictWriter
from datetime import datetime
from pathlib import Path
from sys import stderr

import requests


class ApiService:
    STORAGE_DIR = Path("storage")

    def __init__(self):
        self.endpoint: str = os.environ.get(
            "TODO_ENDPOINT", "https://jsonplaceholder.typicode.com/todos/"
        )
        self.filename_template: str = datetime.now().strftime("%Y_%m_%d") + "_{}.csv"

    def _fetch_data(self):
        response = requests.get(self.endpoint)

        if not response.ok:
            print(
                f"Request to {self.endpoint} failed with status {response.status_code}",
                file=stderr,
            )
            return None

        return response.json()

    def _save_data(self, data):
        filename = self.STORAGE_DIR / Path(self.filename_template.format(data["id"]))

        with open(filename, "w") as csv_file:
            writer = DictWriter(csv_file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)

    def run(self):
        print("Running ApiService", file=stderr)

        data = self._fetch_data()
        if not data:
            print("No data to process", file=stderr)
            return

        for todo in data:
            self._save_data(todo)

        print("Finished", file=stderr)
