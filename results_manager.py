import json
import os
from pathlib import Path


class ResultsManager:

    def __init__(self, results=None):
        self.results = results
        self.path = Path(__file__).parent.joinpath("results_storage.json")

    def export_results(self):

        with open(self.path, "w") as output_file:
            json.dump(self.results, output_file)

    def import_results(self):
        if os.path.isfile(self.path):
            with open(self.path, "r") as input_file:
                self.results = json.load(input_file)
