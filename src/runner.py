thonimport json
from extractors.twitch_video_parser import TwitchVideoParser
from outputs.exporters import JSONExporter

def main():
    # Set your search keywords and max items for scraping
    search_params = {
        "keywords": ["war"],
        "maxItems": 30
    }

    # Instantiate the Twitch video parser
    parser = TwitchVideoParser(search_params)
    data = parser.scrape_data()

    # Export the data to JSON
    exporter = JSONExporter()
    exporter.export(data)

if __name__ == "__main__":
    main()