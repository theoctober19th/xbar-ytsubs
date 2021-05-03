#!/usr/bin/env /usr/local/bin/python3

#  <xbar.var>string(YOUTUBE_CHANNEL_ID="YourChannelID"): Your Channel ID.</xbar.var>
#  <xbar.var>string(YOUTUBE_API_KEY="YouTubeAPIKey"): YouTube API key.</xbar.var>

import os
import requests

YOUTUBE_ICON = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADdcAAA3XAUI"\
"om3gAAAMESURBVFhH7VbPS1RRGP2CogkRRAqyoH8gMsW0aX75AyWREFr0CysIgiByIUKL9pEUVus2SZm7CFqUSom1iTZBUdaqWkjawtGiotQ5r/O9+Wbe9HwjL/tBwRw"\
"4vDv3ft853333vntHSijhvwHaZS3apMxplApyfRFWaIzGWtrK4CSkDgk5iJSczCTlLH8PZBIyTD4iJ9j/Gkl5wzGX2ra+FxrD510+BzRXNVRLNU2+ODiDCJP6MylJO83"\
"i5NnkY2MR+uMKNFhImoX1My5idkvBSnucFktOLiUFEIZBua4mtRfj0mt2P4KVrWaV9zUoSPR3ULX5dsedOlljth4Qk00Meoam4OQ8U+QOY8L6wpLaXOKJL3HZYrYenJj"\
"UMGgKjQGJOaphlDy9B+jaClSz3WBjYUhtFjDDdoPZeliISTMNvrozDEpWagFqOn4TmH0PXDzFWZVl+3aRy+UqOc4CsJCSDrP1QPH2XNCSxBxzBYwOIY+nD4HeDqCe/TU"\
"WE5Rr1M1Ij/1m64Gdne7rD1PA8KC5GxbmgTtXgcPVQC3HYxYfxBYyJUfN1gMPin1o9gX7mS/ghjn78PkDMNgHtHJZdK8EadBjMSnHzdYDP8NfL+DjDDB0AWgrL16AvoG"\
"EHDNbD7oEepqtbAm+AbevAIf4Zeg+WG4JspM8YLYe2LnbDQhTwEjBJnwyBvS0Z88FXX+NCcpVUttJicMvrtNsPThxaeIFEu4zfHALSE8D509QNJLt01kvl6vMjs9zv7W"\
"arQfEZTsLeBfqIDqzFzjCHb+N7Z02FobZg2iahdSarQcGVHHwbxzFzzmJzWbrQS8jXhT3Ql1GP2tsNO2xwMtIQeE/fh3zDQZfxwq+mnUs4hKDZgv/TLjJhfT/EcnRH1e"\
"gwbc7xz12WT3Mrjh4sdTztOpaTEg3CzrHdbvG5wgFHnOGL8m3LHKSnDJOah/jXmkMOcr2de72PuZ1c6xrPhpwA4aFI7KKM4zwUyufi0olRTd8qpeNFK5Sum32cXaVGqO"\
"xmmPpJZTwL0PkOxoj5CNBuCXOAAAAAElFTkSuQmCC"

class YouTubeSubsCounter():

    def __init__(self):
        self.channel_id = os.getenv('YOUTUBE_CHANNEL_ID')
        if not self.channel_id:
            raise EnvironmentError("YOUTUBE_CHANNEL_ID variable not set.")

        self.api_key = os.getenv('YOUTUBE_API_KEY')
        if not self.api_key:
            raise EnvironmentError("YOUTUBE_API_KEY variable not set.")

    def fetch_stats(self):
        try:
            url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
            response = requests.get(url)
            result = response.json()
            items = result.get('items')
            item = items[0]
            statistics = item.get('statistics')
            return statistics
        except:
            return {
                "viewCount": "---",
                "subscriberCount": "---",
                "hiddenSubscriberCount": False,
                "videoCount": "---"
            }
            
    def digest(self):
        stats = self.fetch_stats()
        subs_count = stats.get('subscriberCount')
        views_count = stats.get('viewCount')
        video_count = stats.get('videoCount')
        print("{} subscribers | image={}".format(subs_count, YOUTUBE_ICON))
        print("---")
        print("Refresh|refresh=true")
        print("---")
        print("Channel Statistics")
        print(" #Views:", views_count)
        print(" #Videos:", video_count)
        print("---")
        print("View Source|href=https://github.com/theoctober19th/xbarplugin-ytsubs")
        print("---")
        print("Author: Bikalpa Dhakal 2021")

def main():
    YouTubeSubsCounter().digest()


if __name__ == "__main__":
    main()