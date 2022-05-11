import os
from csv import DictWriter
from datetime import datetime
from pathlib import Path
from sys import stderr

import requests


class DataFetcher:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def fetch_data(self):
        response = requests.get(self.endpoint)

        if not response.ok:
            print(
                f"Request to {self.endpoint} failed with status {response.status_code}",
                file=stderr,
            )
            return None

        return response.json()


class DataSaver:
    STORAGE_DIR = Path("storage")

    def __init__(self):
        self.filename_template = datetime.now().strftime("%Y_%m_%d") + "_{}.csv"

    def save_data(self, data, id_field="id"):
        filename = self.STORAGE_DIR / Path(
            self.filename_template.format(data[id_field])
        )

        with open(filename, "w") as csv_file:
            writer = DictWriter(csv_file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)


class ApiService:
    def __init__(self):
        self.fetcher = DataFetcher(
            os.environ.get(
                "API_ENDPOINT", "https://jsonplaceholder.typicode.com/todos/"
            )
        )
        self.storage = DataSaver()

    def run(self):
        print("Running ApiService", file=stderr)

        fetched_data = self.fetcher.fetch_data()

        if not fetched_data:
            print("No data to process", file=stderr)
            return

        id_field = os.environ.get("ID_FIELD", "id")

        for data in fetched_data:
            self.storage.save_data(data, id_field)

        print("Finished", file=stderr)
