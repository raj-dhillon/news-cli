import json
import os


class ResultsManager:

    def __init__(self, results=None):
        self.results = results

    def export_results(self):
        with open("./results_storage.json", "w") as output_file:
            json.dump(self.results, output_file)

    def import_results(self):
        if os.path.isfile("./results_storage.json"):
            with open("./results_storage.json", "r") as input_file:
                self.results = json.load(input_file)
