thonimport json

class JSONExporter:
    def export(self, data):
        with open('output.json', 'w') as f:
            json.dump(data, f, indent=4)