thonimport requests

class TwitchVideoParser:
    def __init__(self, search_params):
        self.search_params = search_params
        self.base_url = "https://api.twitch.tv/helix/videos"

    def scrape_data(self):
        videos = []
        for keyword in self.search_params["keywords"]:
            response = self._get_video_data(keyword)
            if response:
                videos.extend(self._parse_video_data(response))
        return videos

    def _get_video_data(self, keyword):
        params = {
            "query": keyword,
            "first": self.search_params["maxItems"]
        }
        response = requests.get(self.base_url, params=params)
        return response.json() if response.status_code == 200 else None

    def _parse_video_data(self, data):
        parsed_videos = []
        for video in data['data']:
            parsed_video = {
                "id": video['id'],
                "title": video['title'],
                "viewCount": video['view_count'],
                "createdAt": video['created_at'],
                "game": video['game_name'],
                "creator": {
                    "id": video['user_id'],
                    "displayName": video['user_name']
                }
            }
            parsed_videos.append(parsed_video)
        return parsed_videos